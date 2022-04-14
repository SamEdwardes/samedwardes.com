from typing import Optional, List

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
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

db = DataBase(
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
manager =  LoginManager(SECRECT, "/login")

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
def index(request: Request, user: Optional[User] = None):
    context = {
        "request": request,
        "user": user,
    }
    return templates.TemplateResponse("index.html", context)


# --------------------------------------------------------------------------
# Login
# --------------------------------------------------------------------------
@app.get("/login", response_class=HTMLResponse)
def read_item(request: Request):
    context = {
        "request": request,
        "user": None,
    }
    return templates.TemplateResponse("login.html", context)


@app.post("/login", response_class=HTMLResponse)
def read_item(request: Request, email: str = Form(...), password: str = Form(...)):
    console.rule(request.url.path)
    console.print(locals())
    user = User(email=email, password=password)
    context = {
        "request": request,
        "user": user,
    }
    return RedirectResponse("/")
    # return templates.TemplateResponse("index.html", context)

