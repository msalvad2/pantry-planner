from .database import SessionLocal
from . import models
from . import crud




def main():
    db = SessionLocal()
    # ingredients for making a quesadilla
    item1 = crud.get_or_create_ingredient(db, "Cheese")
    item2 = crud.get_or_create_ingredient(db, "Tortilla")
    item3 = crud.get_or_create_ingredient(db, "Butter")
    

    # ingredients fro making tacos
    item4 = crud.get_or_create_ingredient(db, "Beef")
    item5 = crud.get_or_create_ingredient(db, "Green Sauce")
    item6 = crud.get_or_create_ingredient(db, "Cheese")
    item7 = crud.get_or_create_ingredient(db, "tortilla")

    recipe = models.Recipe(name = "Quesadilla", 
                           instructions = "Put cheese inside and cook on stove for 5 mings",
                            time_minutes = 5,
                            tags = "Under 30 minutes"
                           )
    recipe2 = models.Recipe(name ="Tacos",
                            instructions = "Put ingredients inside then put on stove for 10 minutes",
                            time_minutes = 10,
                            tags = "Under 30 minutes"
    )

    #add recipes to database
    db.add_all([recipe,recipe2])
    db.commit()
    db.refresh(recipe)
    db.refresh(recipe2)

 



    #  id = Column(Integer, primary_key=True, index=True)
    # recipe_id = Column(Integer, ForeignKey("recipes.id"), nullable=False)
    # ingredient_id = Column(Integer, ForeignKey("ingredients.id"), nullable=False)
    # quantity = Column(String, nullable=True)
    # unit = Column(String, nullable=True)

    #maps ingredients to recipe

    #quesadilla mapping (many to many relatinonship)
    cheese_ques_item = models.RecipeIngredient(
        recipe_id = recipe.id,
        ingredient_id = item1.id,
        quantity = "5",
        unit = "Ounces"
    )
    tortilla_ques_item = models.RecipeIngredient(
        recipe_id = recipe.id,
        ingredient_id = item2.id,
        quantity = "2",
        unit = "Tortillas"
    )
    butter_ques_item = models.RecipeIngredient(
        recipe_id = recipe.id,
        ingredient_id = item3.id,
        quantity = "1",
        unit = "Bars"
    )

    #taco mapping
    beef_tac_item = models.RecipeIngredient(
        recipe_id = recipe2.id,
        ingredient_id = item4.id,
        quantity = "1/4",
        unit = "lbs"
    )
    sauce_tac_item = models.RecipeIngredient(
        recipe_id = recipe2.id,
        ingredient_id = item5.id,
        quantity = "1",
        unit = "cups"
    )
    cheese_tac_item = models.RecipeIngredient(
        recipe_id = recipe2.id,
        ingredient_id = item6.id,
        quantity = "2",
        unit = "ounces"
    )

    tortilla_tac_item = models.RecipeIngredient(
        recipe_id = recipe2.id,
        ingredient_id = item7.id,
        quantity = "2",
        unit = "tortilla"
    )
    #add changes and commit to the RecipeIngredient table
    db.add_all([cheese_ques_item, tortilla_ques_item, butter_ques_item, beef_tac_item, sauce_tac_item, cheese_tac_item, tortilla_tac_item])
    db.commit()
    
    # display to confirm success
    print(f"Seeded recipe: {recipe.name} with the following ingredients:")
    for recipe_ingredient in db.query(models.RecipeIngredient).filter(models.RecipeIngredient.recipe_id == recipe.id).all():
        ingredient = db.get(models.Ingredient, recipe_ingredient.ingredient_id)
        if ingredient:
            print("-", ingredient.name, recipe_ingredient.quantity, recipe_ingredient.unit)
    print(f"------------------------------------------------------------------------------------")
    print(f"Seeded recipe: {recipe2.name} with the following ingredients:")
    for recipe_ingredient in db.query(models.RecipeIngredient).filter(models.RecipeIngredient.recipe_id == recipe2.id).all():
        ingredient = db.get(models.Ingredient, recipe_ingredient.ingredient_id)
        if ingredient:
            print("-", ingredient.name, recipe_ingredient.quantity, recipe_ingredient.unit)

    

    db.close()



if __name__ == "__main__":
    main()