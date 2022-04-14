from distutils.log import Log
from typing import Optional, List

from fastapi import FastAPI, Request, Form, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm
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
    email: str
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
        User(email="user1@gmail.com", password="12345"),
        User(email="user2@gmail.com", password="12345"),
    ]
)



# --------------------------------------------------------------------------
# Setup FastAPI
# --------------------------------------------------------------------------
app = FastAPI()
templates = Jinja2Templates(directory="templates")
SECRECT = "7c33ead4881bb004dc2959518f2cf7dd7bdb28a26be7009b"
manager =  LoginManager(SECRECT, "/login/get_token")


@manager.user_loader()
def query_user(email: str) -> User:
    user = [user for user in DB.user if user.email == email]
    if user:
        return user[0]
    else:
        return None

# @app.on_event("startup")
# async def app_init():
#     client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
#     database_names = await client.list_database_names()
    

    
#     if create_demo_data:
#         print("Creating demo data...")
#         await create_data()


# --------------------------------------------------------------------------
# Home Page
# --------------------------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
def index(request: Request, user: User = Depends(manager)):
    console.rule(f"{request.method} ~ {request.url.path}")
    context = {
        "request": request,
        "user": user,
    }
    return templates.TemplateResponse("index.html", context)


# --------------------------------------------------------------------------
# Authentication
# --------------------------------------------------------------------------
@app.get("/login", response_class=HTMLResponse)
def login(request: Request):
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
        self.username = form.get(
            "email"
        )  # since outh works on username field we are considering email as username
        self.password = form.get("password")

    async def is_valid(self):
        if not self.username or not (self.username.__contains__("@")):
            self.errors.append("Email is required")
        if not self.password or not len(self.password) >= 4:
            self.errors.append("A valid password is required")
        if not self.errors:
            return True
        return False


@app.post("/login", response_class=HTMLResponse)
async def login(request: Request):
    console.rule(f"{request.method} ~ {request.url.path}")
    form = LoginForm(request)
    await form.load_data()
    if await form.is_valid():
        


    context = {
        "request": request,
        "user": None,
    }
    return templates.TemplateResponse("login.html", context)




@app.post('/login/get_token')
def login(request: Request, data: OAuth2PasswordRequestForm = Depends()):
    console.rule(f"{request.method} ~ {request.url.path}")

    email = data.username
    password = data.password
    user = query_user(email)
    inspect(user, title="user")

    if not user:
        console.log(f"[red bold]User {email} not found")
        raise InvalidCredentialsException
    elif password != user.password:
        console.log(f"[red bold]Password does not match!")
        raise InvalidCredentialsException
    else:
        console.log("[green] Auth successful!")
    access_token = manager.create_access_token(
        data={'sub': email}
    )
    return {'access_token': access_token, "token_type": "bearer"}

