from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware


#Creates the backend server
app = FastAPI(title= "Mini Pantry API")

#gives the frontend permission to give requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ItemCreate(BaseModel):
    name: str

#list of items
pantry_items = [
    {"id": 1, "name": "milk"},
    {"id": 2, "name": "bread"},
    {"id": 3, "name": "cheese"}
]

# Determine the next ID safely | Will run once when FastAPI starts
next_id = 1

if pantry_items:
    for item in pantry_items:
        if item["id"] >= next_id:
            next_id = item["id"] + 1


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

#adds a new item to the pantry list
@app.post("/pantry", status_code= 201)
def create_pantry_item(item: ItemCreate):
    global next_id

    #confirm empty item won't be added
    cleaned = item.name.strip().lower()
    if cleaned == "":
        raise HTTPException(
            status_code= 400,
            detail= "Item name cannot be empty"
        )

    new_item = {"id": next_id, "name": cleaned}
    pantry_items.append(new_item)
    #update the next id after each request
    next_id += 1

    return new_item

#update item in list using id
@app.put("/pantry/{item_id}")
def update_pantry_item(item_id: int, updated_item: ItemCreate):
    cleaned = updated_item.name.strip().lower()

    if cleaned == "":
        raise HTTPException(
            status_code= 400,
            detail="Item name cannot be empty"
        )
    
    for item in pantry_items:
        if item["id"] == item_id:
            item["name"] = cleaned
            return item
        
    raise HTTPException(
        status_code= 404,
        detail="Item not found"
    )
#remove item from list using id

@app.delete("/pantry/{item_id}", status_code=204)
def remove_pantry_item(item_id: int):
    for i, item in enumerate(pantry_items):
        if item["id"] == item_id:
            pantry_items.pop(i)
            return
    raise HTTPException(
        status_code=404,
        detail="Item not found"
    )
