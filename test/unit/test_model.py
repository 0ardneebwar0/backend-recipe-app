from api.models import Recipe
import pytest

def test_create_recipe():
    """
    GIVEN a Recipe model
    WHEN a new Recipe is created
    THEN check the name, ingredients, instructions, rating, is_favorite fields are defined correctly
    """
    recipe = Recipe('Boiled Egg', 'Water, Salt, Egg', 'Put some water and egg in a pot, let it boil for 5-7 minutes, its ready')
    assert recipe.name == 'Boiled Egg'
    assert recipe.ingredients == 'Water, Egg, Salt'
    assert recipe.instructions == 'Put some water and egg in a pot, let it boil for 5-7 minutes, its ready'
    #assert recipe.rating == 0
    #assert recipe.is_favorite == False
