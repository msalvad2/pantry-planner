from .database import Base, engine
from . import models
from sqlalchemy import inspect

def init_db():
    print("Creating tables...")
    # will create database tables based on teh SQL modes, only if the tables
    # don't already exist, it's safe to modify since it only adds not deletes
    Base.metadata.create_all(bind=engine)

    print("Done!")

    #checks to see if it created the tables correctly
    # inspector = inspect(engine)
    # print("Tables:", inspector.get_table_names())


if __name__ == "__main__":
    init_db()