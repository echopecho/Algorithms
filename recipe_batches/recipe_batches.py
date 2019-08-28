#!/usr/bin/python

import math


def recipe_batches(recipe, ingredients):
    servings = []
    for item in recipe.keys():
        num = ingredients[item] // recipe[item]
        servings.append(num)
    return min(servings)


if __name__ == "__main__":
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    # {"milk": 2, "sugar": 40, "butter": 20}, {"milk": 5, "sugar": 120, "butter": 500}
    recipe = {"milk": 2, "sugar": 40, "butter": 20}
    ingredients = {"milk": 5, "sugar": 120, "butter": 500}
    print(
        "{batches} batches can be made from the available ingredients: {ingredients}.".format(
            batches=recipe_batches(recipe, ingredients), ingredients=ingredients
        )
    )

