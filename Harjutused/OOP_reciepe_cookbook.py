"""
Lisa meetod get_recipe_ingredients, mis tagastab järjendi koostisosadest, kui selline restsept on olemas.
Kui retsepti pole, tagastab meetod tühja järjendi.
"""


class Recipe:
    def __init__(self, name: str, ingredients: list[str]):
        self.name = name
        self.ingredients = ingredients

    def add_ingredient(self, ingredient: str):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, ingredient: str):
        if ingredient in self.ingredients:
            self.ingredients.remove(ingredient)


class Cookbook:
    def __init__(self):
        self.recipes = {}

    def add_recipe(self, recipe: Recipe):
        self.recipes[recipe.name] = recipe

    def get_recipe_ingredients(self, recipe_name: str):
        if recipe_name in self.recipes:
            return self.recipes[recipe_name].ingredients
        return []


cookbook = Cookbook()
pizza_recipe = Recipe("Pizza", ["Dough", "Tomato Sauce"])
cookbook.add_recipe(pizza_recipe)
ingredients = cookbook.get_recipe_ingredients("Pizza")
print(ingredients == ["Dough", "Tomato Sauce"])