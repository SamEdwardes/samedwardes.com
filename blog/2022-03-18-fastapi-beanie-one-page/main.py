from typing import Optional

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from beanie import Document, Link, init_beanie
import motor

# --------------------------------------------------------------------------
# Define your models with Beanie
# --------------------------------------------------------------------------
class Breed(Document):
    name: str
    description: Optional[str]
    country_of_origin: str
    average_weight: Optional[int]
    image_url: str = "imgs/placeholder_square.jpeg"


class Dog(Document):
    name: str
    description: Optional[str]
    breed: Link[Breed]
    owner: str
    image_url: str = "imgs/placeholder_square.jpeg"
    
    
async def create_data():
    """A helper function to insert demo/starter data into your database."""
    # Create some breeds
    min_pin = Breed(
        name="Miniature Pinscher", 
        country_of_origin="Germany", 
        average_weight=10
    )
    
    golden = Breed(
        name="Golden Retrevier", 
        country_of_origin="United States", 
        average_weight=50
    )
    
    # Create some dogs
    roo = Dog(
        name="Roo", 
        breed=min_pin, 
        owner="Sam", 
        description="A feisty little guy who is not afraid to speak his mind."
    )
    
    pepper = Dog(
        name="Pepper", 
        breed=min_pin, 
        owner="Allie",
        description="Roo's twin brother. Name is pronounced as 'Peppa'."
    )
    
    buddy = Dog(
        name="Buddy", 
        breed=golden, 
        owner="Olivia",
        description="Your everyday average goodboy."
    )
    
    # Insert data into the database.
    for document in [min_pin, golden, roo, pepper, buddy]:
        await document.insert()

# --------------------------------------------------------------------------
# Setup Fast API and MongoDB database
# --------------------------------------------------------------------------
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
@app.on_event("startup")
async def app_init():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    client.drop_database("dogs")
    app.db = client.dogs
    await init_beanie(database=app.db, document_models=[Breed, Dog])
    await create_data()

# --------------------------------------------------------------------------
# Routes
# --------------------------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    dogs = await Dog.find_all().to_list()
    breeds = await Breed.find_all().to_list()
    context = {
        "request": request,
        "breeds": breeds
    }
    return templates.TemplateResponse("index.html", context)


@app.get("/breeds", response_class=HTMLResponse)
async def read_item(request: Request):
    breeds = await Breed.find_all().to_list()
    context = {
        "request": request,
        "breeds": breeds
    }
    return templates.TemplateResponse("breeds.html", context)


@app.get("/breeds/{breed_id}")
async def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}


@app.get("/dogs", response_class=HTMLResponse)
async def read_item(request: Request):
    dogs = await Dog.find_all().to_list()
    context = {
        "request": request,
        "dogs": dogs
    }
    return templates.TemplateResponse("dogs.html", context)

@app.get("/dogs/{dog_id}", response_class=HTMLResponse)
async def read_item(dog_id: str, request: Request):
    dog = await Dog.get(dog_id, fetch_links=True)
    print(dog)
    context = {
        "request": request,
        "dog": dog
    }
    return templates.TemplateResponse("dog_profile.html", context)


