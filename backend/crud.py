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
