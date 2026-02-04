# fastapi
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
# pydantic
from .schemas import ItemCreate, RecipeOut, RecipeSummary
# sqlalchemy
from sqlalchemy.orm import Session
# local module
from .database import SessionLocal
from . import crud


# creates new session, gives it to the route, and closes it automatically
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

#Creates the backend server
app = FastAPI(title= "Mini Pantry API")

#gives the frontend permission to make requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


#returns all of the pantry items
@app.get("/pantry")
def get_pantry_items(db: Session = Depends(get_db)):
    return crud.list_pantry_items(db)

#returns specific item based on item id
@app.get("/pantry/{item_id}")
def get_pantry_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.get_pantry_item(db, item_id)

    if item is None:
        raise HTTPException(
            status_code= 404,
            detail= "Item not Found"
        )
    return item

#adds a new item to the pantry lists
@app.post("/pantry", status_code= 201)
def create_pantry_item(item: ItemCreate, db: Session = Depends(get_db)):

    #confirm empty item won't be added
    cleaned = item.name.strip().lower()
    if cleaned == "":
        raise HTTPException(
            status_code= 400,
            detail= "Item name cannot be empty"
        )

    new_item = crud.create_pantry_item(db, cleaned)

    return new_item

#update item in list using id
@app.put("/pantry/{item_id}")
def update_pantry_item(item_id: int, updated_item: ItemCreate, db: Session = Depends(get_db)):
    cleaned = updated_item.name.strip().lower()

    if cleaned == "":
        raise HTTPException(
            status_code= 400,
            detail="Item name cannot be empty"
        )
    
    item = crud.update_pantry_item(db, item_id, cleaned)
    
    if item is None:
        raise HTTPException(
            status_code= 404,
            detail="Item not found"
        )
    return item

#remove item from list using id
@app.delete("/pantry/{item_id}", status_code=204)
def remove_pantry_item(item_id: int, db: Session = Depends(get_db)):
    item = crud.delete_pantry_item(db, item_id)
    
    if item is None:
        raise HTTPException(
            status_code=404,
            detail="Item not found"
        )

######recipe#########

#gets a recipe with its information
@app.get("/recipes/{recipe_id}", response_model=RecipeOut)

def get_recipe(recipe_id: int, db:Session = Depends(get_db)):
    recipe = crud.get_recipe_with_ingredients(db, recipe_id)
    if recipe is None:
        raise HTTPException(
            status_code=404,
            detail="Recipe not found"
        )
    return recipe

@app.get("/recipes", response_model=list[RecipeSummary])

def get_recipes(db: Session = Depends(get_db)):
    return crud.get_all_recipes(db)





















