from .database import SessionLocal
from . import crud


def main():
    # start the session
    db = SessionLocal()

    # creates items 
    crud.create_pantry_item(db, "Flour")
    crud.create_pantry_item(db, "Syrup")
    crud.create_pantry_item(db, "Sugar")

    # lists items in db
    item_list = crud.list_pantry_items(db)

    for item in item_list:
        print(f"Item: {item.name}, ID: {item.id}")

    # get specific item by id
    item = crud.get_pantry_item(db, 4)
    
    if item is None:
        print("Item not found")
    else:
        print(f"Item: {item.name}, {item.id}")

    #remove item using id

    crud.delete_pantry_item(db, 4)
    crud.delete_pantry_item(db, 5)
    crud.delete_pantry_item(db, 6)
    crud.delete_pantry_item(db,7)    

    items = crud.list_pantry_items(db)
    print("After removing")
    for item in items:
         print(f"Item: {item.name}, ID: {item.id}")

    # ends the session
    db.close()


if __name__ == "__main__":
    main()