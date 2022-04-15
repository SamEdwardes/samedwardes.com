from distutils.log import Log
from typing import Dict, Optional, List
import datetime as dt
from jose import jwt, JWTError

from fastapi import FastAPI, Request, Form, Depends, Response, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer, OAuth2
from fastapi_login.exceptions import InvalidCredentialsException
from fastapi.openapi.models import OAuthFlows as OAuthFlowsModel
from fastapi.templating import Jinja2Templates
from fastapi_login import LoginManager
from pydantic import BaseModel
from rich.console import Console
from rich import inspect
from fastapi.security.utils import get_authorization_scheme_param

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
    COOKIE_NAME = "access_token"


class OAuth2PasswordBearerWithCookie(OAuth2):
    def __init__(
        self,
        tokenUrl: str,
        scheme_name: Optional[str] = None,
        scopes: Optional[Dict[str, str]] = None,
        auto_error: bool = True,
    ):
        # //////////////////////
        console.rule(f"OAuth2PasswordBearerWithCookie.__init__()", characters="~", style="yellow")
        console.log(locals())
        # //////////////////////
        if not scopes:
            scopes = {}
        flows = OAuthFlowsModel(password={"tokenUrl": tokenUrl, "scopes": scopes})
        super().__init__(flows=flows, scheme_name=scheme_name, auto_error=auto_error)

    async def __call__(self, request: Request) -> Optional[str]:
        # //////////////////////
        console.rule(f"OAuth2PasswordBearerWithCookie.__call__()", characters="~", style="yellow")
        console.log(locals())
        # //////////////////////
        authorization: str = request.cookies.get(settings.COOKIE_NAME)  # changed to accept access token from httpOnly Cookie
        print("access_token is", authorization)
        scheme, param = get_authorization_scheme_param(authorization)
        if not authorization or scheme.lower() != "bearer":
            if self.auto_error:
                raise HTTPException( status_code=status.HTTP_401_UNAUTHORIZED, detail="Not authenticated", headers={"WWW-Authenticate": "Bearer"},)
            else:
                return None
        return param


app = FastAPI()
templates = Jinja2Templates(directory="templates")
oauth2_scheme = OAuth2PasswordBearerWithCookie(tokenUrl="/auth/token")
settings = Settings()


# --------------------------------------------------------------------------
# Authentication logic
# --------------------------------------------------------------------------
def create_access_token(data: Dict):
    # //////////////////////
    console.rule(f"create_access_token()", characters="~", style="yellow")
    console.log(locals())
    # //////////////////////
    to_encode = data.copy()
    expire = dt.datetime.utcnow() + dt.timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(
        to_encode, 
        settings.SECRET_KEY, 
        algorithm=settings.ALGORITHM
    )
    return encoded_jwt


def get_user(username: str) -> User:
    # //////////////////////
    console.rule(f"get_user()", characters="~", style="yellow")
    console.log(locals())
    # //////////////////////
    user = [user for user in DB.user if user.username == username]
    if user:
        return user[0]
    return None


def authenticate_user(username: str, password: str) -> User:
    # //////////////////////
    console.rule(f"authenticate_user()", characters="~", style="yellow")
    console.log(locals())
    # //////////////////////
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


def get_current_user_from_token(token: str = Depends(oauth2_scheme)) -> User:
    # //////////////////////
    console.rule(f"get_current_user_from_token()", characters="~", style="yellow")
    console.log(locals())
    # //////////////////////
    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate credentials",)
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        console.log(locals())
        print("username/email extracted is ", username)
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = get_user(username)
    if user is None:
        raise credentials_exception
    return user


def get_user_from_cookie(request: Request):
    # //////////////////////
    console.rule(f"get_user_from_cookie()", characters="~", style="yellow")
    console.log(locals())
    # //////////////////////
    token = request.cookies.get(settings.COOKIE_NAME)
    token = token.removeprefix("Bearer").strip()
    user = get_current_user_from_token(token)
    return user


@app.post("/auth/token")
def login_for_access_token(
    response: Response, 
    form_data: OAuth2PasswordRequestForm = Depends()
):
    # //////////////////////
    console.rule("POST ~ /auth/token")
    console.log(locals())
    # //////////////////////
    user = authenticate_user(form_data.username, form_data.password)
    if not user:
        console.log("[red bold]User not authenticated!")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Incorrect username or password",)
    console.log("Creating access token...")
    access_token = create_access_token(data={"sub": user.username})
    response.set_cookie(key=settings.COOKIE_NAME, value=f"Bearer {access_token}", httponly=True)  #set HttpOnly cookie in response
    console.log("Cookie set!")
    return {settings.COOKIE_NAME: access_token, "token_type": "bearer"}


# --------------------------------------------------------------------------
# Home Page
# --------------------------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
def index(request: Request):
    # //////////////////////
    console.rule(f"{request.method} ~ {request.url.path}")
    console.log(locals())
    # //////////////////////
    try:
        user = get_user_from_cookie(request)
        console.log(f"{user=}")
        console.log("[green]user found!")
    except:
        user = None
        console.log("[red]user not found")
    context = {
        "user": user,
        "request": request,
    }
    return templates.TemplateResponse("index.html", context)


@app.post("/", response_class=HTMLResponse)
def index(request: Request, user: User):
    # //////////////////////
    console.rule(f"{request.method} ~ {request.url.path}")
    console.log(locals())
    # //////////////////////
    try:
        user = get_user_from_cookie(request)
        console.log(f"{user=}")
        console.log("[green]user found!")
    except:
        user = None
        console.log("[red]user not found")
    context = {
        "user": user,
        "request": request,
    }
    return templates.TemplateResponse("index.html", context)


# --------------------------------------------------------------------------
# Private Page
# --------------------------------------------------------------------------
# A private page that only logged in users can access.
@app.get("/private", response_class=HTMLResponse)
def index(request: Request, user: User = Depends(get_current_user_from_token)):
    # //////////////////////
    console.rule(f"{request.method} ~ {request.url.path}")
    console.log(locals())
    # //////////////////////
    context = {
        "user": user,
        "request": request
    }
    return templates.TemplateResponse("private.html", context)

# --------------------------------------------------------------------------
# Authentication
# --------------------------------------------------------------------------
@app.get("/auth/login", response_class=HTMLResponse)
def login_get(request: Request):
    # //////////////////////
    console.rule(f"{request.method} ~ {request.url.path}")
    console.log(locals())
    # //////////////////////
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
    # //////////////////////
    console.rule(f"{request.method} ~ {request.url.path}")
    console.log(locals())
    # //////////////////////
    form = LoginForm(request)
    await form.load_data()
    console.log(form.__dict__)
    if await form.is_valid():
        try:
            form.__dict__.update(msg="Login Successful!")
            # user = get_user(form.username)
            # context = {
            #     "user": user,
            #     "request": request,
            # }
            # response = templates.TemplateResponse("index.html", form.__dict__)
            response = RedirectResponse("/", status.HTTP_302_FOUND)
            _ = login_for_access_token(response=response, form_data=form)
            inspect(_)
            console.log("[green]Login successful!!!!")
            return response
        except HTTPException:
            form.__dict__.update(msg="")
            form.__dict__.get("errors").append("Incorrect Email or Password")
            return templates.TemplateResponse("login.html", form.__dict__)
    return templates.TemplateResponse("login.html", form.__dict__)


@app.get("/auth/logout", response_class=HTMLResponse)
def login_get():
    # //////////////////////
    console.rule(f"GET ~ /auth/logout")
    console.log(locals())
    # //////////////////////
    response = RedirectResponse(url="/")
    response.delete_cookie(settings.COOKIE_NAME)
    return response
