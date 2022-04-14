from distutils.log import Log
from typing import Optional, List
import datetime as dt
from jose import jwt

from fastapi import FastAPI, Request, Form, Depends, Response, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi.templating import Jinja2Templates
from fastapi_login import LoginManager
from pydantic import BaseModel
from rich.console import Console
from rich import inspect

console = Console()


# --------------------------------------------------------------------------
# Models
# --------------------------------------------------------------------------
class User(BaseModel):
    username: str
    password: str




# --------------------------------------------------------------------------
# Database
# --------------------------------------------------------------------------
# Create a "database" to hold your data. This is just for example purposes to
# quickly show this proof of conept app.
class DataBase(BaseModel):
    user: List[User]

DB = DataBase(
    user=[
        User(username="user1@gmail.com", password="12345"),
        User(username="user2@gmail.com", password="12345"),
    ]
)



# --------------------------------------------------------------------------
# Setup FastAPI
# --------------------------------------------------------------------------
class Settings:
    SECRET_KEY: str = "secret-key"
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30  # in mins


app = FastAPI()
templates = Jinja2Templates(directory="templates")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/login/token")
settings = Settings()


# --------------------------------------------------------------------------
# Authentication logic
# --------------------------------------------------------------------------
def create_access_token(
    data: dict, 
    expires_delta: Optional[dt.timedelta] = None
):
    console.log("create_access_token()")
    to_encode = data.copy()
    if expires_delta:
        expire = dt.datetime.utcnow() + expires_delta
    else:
        expire = dt.datetime.utcnow() + dt.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def get_user(username: str) -> User:
    user = [user for user in DB.user if user.username == username]
    if user:
        return user[0]
    else:
        return None


def authenticate_user(username: str, password: str) -> User:
    user = get_user(username)
    console.log(locals())
    # (1) Validate if the user exists.
    if not user:
        return False
    # (2) Validate if the
    # TODO: hash the password
    elif password != user.password:
        return False
    else:
        return user


@app.post("/auth/token")
def login_for_access_token(
    response: Response, 
    form_data: OAuth2PasswordRequestForm = Depends()
):
    console.log("login_for_access_token()")
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password",)
    access_token_expires = dt.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    response.set_cookie(key="access_token",value=f"Bearer {access_token}", httponly=True)  #set HttpOnly cookie in response
    return {"access_token": access_token, "token_type": "bearer"}

# --------------------------------------------------------------------------
# Home Page
# --------------------------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    console.rule(f"{request.method} ~ {request.url.path}")
    context = {
        "request": request,
    }
    return templates.TemplateResponse("index.html", context)


# --------------------------------------------------------------------------
# Authentication
# --------------------------------------------------------------------------
@app.get("/auth/login", response_class=HTMLResponse)
def login_get(request: Request):
    console.rule(f"{request.method} ~ {request.url.path}")
    context = {
        "request": request,
        "user": None,
    }
    return templates.TemplateResponse("login.html", context)


class LoginForm:
    def __init__(self, request: Request):
        self.request: Request = request
        self.errors: List = []
        self.username: Optional[str] = None
        self.password: Optional[str] = None

    async def load_data(self):
        form = await self.request.form()
        self.username = form.get("username")  # since outh works on username field we are considering email as username
        self.password = form.get("password")

    async def is_valid(self):
        if not self.username or not (self.username.__contains__("@")):
            self.errors.append("Email is required")
        if not self.password or not len(self.password) >= 4:
            self.errors.append("A valid password is required")
        if not self.errors:
            return True
        return False


@app.post("/auth/login", response_class=HTMLResponse)
async def login_post(request: Request):
    console.rule(f"{request.method} ~ {request.url.path}")
    form = LoginForm(request)
    await form.load_data()
    console.log(form.__dict__)
    if await form.is_valid():
        try:
            form.__dict__.update(msg="Login Successful!")
            response = templates.TemplateResponse("login.html", form.__dict__)
            login_for_access_token(response=response, form_data=form)
            console.log("[green]Login successful!!!!")
            return response
        except HTTPException:
            form.__dict__.update(msg="")
            form.__dict__.get("errors").append("Incorrect Email or Password")
            return templates.TemplateResponse("login.html", form.__dict__)
    return templates.TemplateResponse("login.html", form.__dict__)




# @app.post('/auth/token')
# def login(request: Request, data: OAuth2PasswordRequestForm = Depends()):
#     console.rule(f"{request.method} ~ {request.url.path}")

#     email = data.username
#     password = data.password
#     user = query_user(email)
#     inspect(user, title="user")

#     if not user:
#         console.log(f"[red bold]User {email} not found")
#         raise InvalidCredentialsException
#     elif password != user.password:
#         console.log(f"[red bold]Password does not match!")
#         raise InvalidCredentialsException
#     else:
#         console.log("[green] Auth successful!")
#     access_token = manager.create_access_token(
#         data={'sub': email}
#     )
#     return {'access_token': access_token, "token_type": "bearer"}

