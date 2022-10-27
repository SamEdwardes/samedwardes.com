from typing import Optional

import motor
from beanie import Document, Link, init_beanie
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


# --------------------------------------------------------------------------
# Step 1: Define your models with Beanie
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

   
# --------------------------------------------------------------------------
# Step 2: Create demo data
# --------------------------------------------------------------------------   
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
        name="Golden Retriever",
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
        description="Your everyday average good boy."
    )
    
    # Insert data into the database.
    for document in [min_pin, golden, roo, pepper, buddy]:
        await document.insert()


# --------------------------------------------------------------------------
# Step 3: Setup FastAPI and MongoDB database
# --------------------------------------------------------------------------
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.on_event("startup")
async def app_init():
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    database_names = await client.list_database_names()
    
    if "dogs" not in database_names:
        create_demo_data = True
    else:
        create_demo_data = False
    
    app.db = client.dogs
    await init_beanie(database=app.db, document_models=[Breed, Dog])
    
    if create_demo_data:
        print("Creating demo data...")
        await create_data()


# --------------------------------------------------------------------------
# Step 4: Home page
# --------------------------------------------------------------------------
@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    context = {
        "request": request,
    }
    return templates.TemplateResponse("index.html", context)


# --------------------------------------------------------------------------
# Step 5: Breeds page
# --------------------------------------------------------------------------
@app.get("/breeds", response_class=HTMLResponse)
async def read_item(request: Request):
    breeds = await Breed.find_all().to_list()
    context = {
        "request": request,
        "breeds": breeds
    }
    return templates.TemplateResponse("breeds.html", context)


# --------------------------------------------------------------------------
# Step 6: Dogs page
# --------------------------------------------------------------------------
@app.get("/dogs", response_class=HTMLResponse)
async def read_item(request: Request, breed_id: Optional[str] = None):
    if breed_id:
        breed = await Breed.get(breed_id)
        dogs = await Dog.find( Dog.breed._id == breed.id, fetch_links=True).to_list()
    else:
        breed = None
        dogs = await Dog.find_all().to_list()
    context = {
        "request": request,
        "dogs": dogs,
        "breed": breed
    }
    return templates.TemplateResponse("dogs.html", context)


# --------------------------------------------------------------------------
# Step 7: Dog page
# --------------------------------------------------------------------------
@app.get("/dogs/{dog_id}", response_class=HTMLResponse)
async def read_item(dog_id: str, request: Request):
    dog = await Dog.get(dog_id, fetch_links=True)
    context = {
        "request": request,
        "dog": dog
    }
    return templates.TemplateResponse("dog_profile.html", context)
