from sqlalchemy.orm import Session
from . import models

# adds item to pantry table
def create_pantry_item(db: Session, name: str):

    item = models.PantryItem(name = name)
    db.add(item)
    db.commit()
    # after commiting database gives item item_id, it gets sent back after refreshing
    db.refresh(item)
    return item

# returns all items in pantry table
def list_pantry_items(db: Session):
    return db.query(models.PantryItem).all()

# returns item searched by item id
def get_pantry_item(db: Session, item_id: int):
    return (
        db.query(models.PantryItem)
            .filter(models.PantryItem.id == item_id)
            .first()
    )

# returns item after updating
def update_pantry_item(db: Session, item_id: int, name: str):
    item = db.query(models.PantryItem).filter(models.PantryItem.id == item_id).first()

    if item is None:
        return None
    #item.name is a class that holds a string and I am assigning it to a string
    item.name = name # type: ignore
    db.commit()
    db.refresh(item)
    return item

# removes item from the pantry table
def delete_pantry_item(db: Session, item_id: int):
    item = db.query(models.PantryItem).filter(models.PantryItem.id == item_id).first()

    if item is None:
        return None
    
    db.delete(item)
    db.commit()

    return item


def get_or_create_ingredient(db: Session, name: str):
    
    cleaned = name.strip().lower()
    #check to see if ingredient exists
    ingredient = db.query(models.Ingredient).filter(models.Ingredient.name == cleaned).first()

    if ingredient is None:
        ingredient = models.Ingredient(name = cleaned)
        db.add(ingredient)
        db.commit()
        db.refresh(ingredient)
        
    
    return ingredient

def get_recipe_with_ingredients(db: Session, recipe_id: int):
    recipe = db.query(models.Recipe).filter(models.Recipe.id == recipe_id).first()

    if recipe is None:
        return None
    #temporarily joins the two tables together and returns them
    rows = (
        db.query(models.RecipeIngredient, models.Ingredient)
        .join(models.Ingredient, models.RecipeIngredient.ingredient_id == models.Ingredient.id)
        .filter(models.RecipeIngredient.recipe_id == recipe_id)
        .all()
    )

    ingredient_list: list[dict] = []
    #adds to the ingredient list with all of its information
    for recipe_ingredient, ingredient in rows:
        ingredient_list.append({
            "id": ingredient.id,
            "name": ingredient.name,
            "quantity": recipe_ingredient.quantity,
            "unit": recipe_ingredient.unit,
        })

    #we follow the format when returning of class RecipeOut(BaseModel)
    return {
        "id": recipe.id,
        "name": recipe.name,
        "time_minutes": recipe.time_minutes,
        "instructions": recipe.instructions,
        "tags": recipe.tags,
        "ingredients":ingredient_list,
    }

def get_all_recipes(db: Session):
    return db.query(models.Recipe).all()