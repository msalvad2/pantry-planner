from pydantic import BaseModel, ConfigDict


#pydantice- shape of data that crosses the API boundary

class ItemCreate(BaseModel):
    name: str
# describes how ingredient appears when attached to a recipe
class IngredientInRecipeOut(BaseModel):
    id: int
    name: str
    quantity: str | None = None
    unit: str | None = None

    #makes this pydantic model compatible with ORM objects and treats them like dicts
    #since it will receive the data from the database
    model_config = ConfigDict(from_attributes=True)

class RecipeOut(BaseModel):
    id: int
    name: str
    #type hint: int or none, default if not provided is None
    time_minutes: int | None = None
    tags: str | None = None
    instructions: str | None = None
    #the recipe contains a list of ingredient objects and the objects must follow,
    #the IngredientInRecipeOut blueprint
    ingredients: list[IngredientInRecipeOut]    

    model_config = ConfigDict(from_attributes=True)
#used when user wants to display all recipes in db
class RecipeSummary(BaseModel):
    id: int
    name: str
    time_minutes: int | None = None

    model_config = ConfigDict(from_attributes=True)

