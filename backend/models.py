from sqlalchemy import Column, Integer, String, Text, ForeignKey, UniqueConstraint
from .database import Base

# table that contains user's ingredient
class PantryItem(Base):
    __tablename__ = "pantry_items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

# table holds all the ingredients the sytems knows about, each row will be unique
class Ingredient(Base):
    __tablename__ = "ingredients"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False, unique=True)

# table that holds recipes
class Recipe(Base):
    __tablename__ = "recipes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    instructions = Column(Text, nullable=True)
    time_minutes = Column(Integer, nullable=True)
    tags = Column(String, nullable=True)

# table that maps the ingredients to the recipes (many to many relationship)
class RecipeIngredient(Base):
    __tablename__ = "recipe_ingredients"

    id = Column(Integer, primary_key=True, index=True)
    recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    ingredient_id = Column(Integer, ForeignKey("ingredients.id"), nullable=False)
    quantity = Column(String, nullable=True)
    unit = Column(String, nullable=True)

    # For all recipes, an ingredient should appear at most once
    __table_args__ = (
        UniqueConstraint("recipe_id", "ingredient_id", name="unique_recipe_ingredient_pair"),
    )