from typing import Optional

from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from beanie import Document, Link, init_beanie
import motor

from rich import inspect

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
        description="A wee bit crazy 🤪",
        country_of_origin="Germany", 
        average_weight=10,
        image_url="imgs/breeds/min-pin.png"
    )
    
    golden = Breed(
        name="Golden Retrevier",
        description="Your everyday average good boy 😇",
        country_of_origin="United States", 
        average_weight=50,
        image_url="imgs/breeds/golden.png"
    )
    
    # Create some dogs
    roo = Dog(
        name="Roo", 
        breed=min_pin, 
        owner="Sam",
        image_url="imgs/dogs/roo.png",
        description="A feisty little guy who is not afraid to speak his mind."
    )
    
    pepper = Dog(
        name="Pepper", 
        breed=min_pin, 
        owner="Allie",
        image_url="imgs/dogs/pepper.png",
        description="Roo's twin brother. Name is pronounced as 'Peppa'."
    )
    
    buddy = Dog(
        name="Buddy", 
        breed=golden, 
        owner="Olivia",
        image_url="imgs/dogs/buddy.png",
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
    # client.drop_database("dogs")
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


@app.get("/dogs", response_class=HTMLResponse)
async def read_item(request: Request, breed_id: Optional[str] = None):
    if breed_id:
        breed = await Breed.get(breed_id)
        inspect(breed, title="breed")
        dogs = await Dog.find(
            Dog.breed.name == breed.name,
            fetch_links=True
        ).to_list()
        inspect(dogs, title="dogs")
    else:
        breed = None
        dogs = await Dog.find_all().to_list()
    context = {
        "request": request,
        "dogs": dogs,
        "breed": breed
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


