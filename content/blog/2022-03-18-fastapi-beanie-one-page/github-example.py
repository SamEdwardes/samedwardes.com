import asyncio
from typing import Optional

import motor
from beanie import Document, Link, init_beanie
from rich.pretty import pprint


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


async def main():
    # Set up the database
    client = motor.motor_asyncio.AsyncIOMotorClient("mongodb://localhost:27017")
    client.drop_database("dogs")
    await init_beanie(database=client.dogs, document_models=[Breed, Dog])
    await create_data()
    
    # Get a breed
    breed = await Breed.find_one(Breed.name == "Miniature Pinscher")
    print("Breed:")
    pprint(breed.__dict__)
    
    # Query by name works:
    dogs_by_name = await Dog.find(Dog.breed.name == breed.name, fetch_links=True).to_list()
    print("Dogs who are min pins (search by name):")
    pprint([i.__dict__ for i in dogs_by_name])
    
    # Query by id does not work. What is wrong?
    dogs_by_id = await Dog.find(Dog.breed.id == breed.id, fetch_links=True).to_list()
    print("Dogs who are min pins (search by id):")
    pprint([i.__dict__ for i in dogs_by_id])
    
    # Try new solution query by _id
    dogs_by_id = await Dog.find(Dog.breed._id == breed.id, fetch_links=True).to_list()
    print("Dogs who are min pins (search by _id):")
    pprint([i.__dict__ for i in dogs_by_id])
    

asyncio.run(main())