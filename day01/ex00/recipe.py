class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        if isinstance(name, str):
            self.name = name
        else:
            print('Type error: name should be a string')
        if isinstance(cooking_lvl, int):
            if cooking_lvl in range(1, 6):
                self.cooking_lvl = cooking_lvl
            else:
                print('Value error: cooking_lvl should be between 1 and 5')
        else:
            print('Type error: cooking_lvl should be an integer')
        if isinstance(cooking_time, int):
            if cooking_time > 0:
                self.cooking_time = cooking_time
            else:
                print('Value error: cooking_time should be a positive integer')
        else:
            print('Type error: cooking_time should be an integer')
        flag = 0
        if isinstance(ingredients, list):
            for elem in ingredients:
                if not isinstance(elem, str):
                    flag = 1
            if flag == 0:
                self.ingredients = ingredients
            elif flag == 1:
                print('Value error: at least one element of ingredients is not a string')
        else:
            print('Type error: ingredients should be a list')
        if description is not None:
            if isinstance(description, str):
                self.description = description
            else:
                print('Type error: description should be a string')
        if isinstance(recipe_type, str):
            if recipe_type in ["starter", "lunch", "dessert"]:
                self.recipe_type = recipe_type
            else:
                print('Value error: recipe_type should be "starter", "lunch" or "dessert"')
        else:
            print('Type error: recipe_type should be a string')

    def __str__(self):
        """Return the string to print with the recipe info"""
        txt = ""
        txt = f'This is the recipe for {self.name}.\n' \
              f'Cooking level: {self.cooking_lvl}\n' \
              f'Cooking time: {self.cooking_time}\n' \
              f'Ingredients: {self.ingredients}\n' \
              f'This recipe is for {self.recipe_type}.\n' \
              f'{self.description}\n'
        return txt
