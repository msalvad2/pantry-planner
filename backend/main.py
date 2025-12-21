from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

#Creates the backend server
app = FastAPI(title= "Mini Pantry API")

#gives the frontend permission to give requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True, #used for login/cookies
    allow_methods=["*"],
    allow_headers=["*"],
)


#list of items
pantry_items = [
    {"id": 1, "name": "milk"},
    {"id": 2, "name": "bread"},
    {"id": 3, "name": "cheese"}
]

#returns all of the pantry items
@app.get("/pantry")
def get_pantry_items():
    return pantry_items

#returns specific item based on item id
@app.get("/pantry/{item_id}")
def get_pantry_item(item_id: int):
    for item in pantry_items:
        if item["id"] == item_id:
            return item
    raise HTTPException(
        status_code= 404,
        detail= "Item not Found"
    )

class ItemCreate(BaseModel):
    name: str

#adds a new item to the pantry list
@app.post("/pantry", status_code= 201)
def create_pantry_item(item: ItemCreate):
    #confirm empty item won't be added
    cleaned = item.name.strip().lower()
    if cleaned == "":
        raise HTTPException(
            status_code= 400,
            detail= "Item name cannot be empty"
        )

    new_item = {"id": len(pantry_items) + 1, "name": cleaned}
    pantry_items.append(new_item)
    return new_item
    
