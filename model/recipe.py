import re
import peewee

from model.configs import db
from model.configs import BaseModel
from model.menu import Menu
from model.ingredient import Ingredient
from exceptions import StructureError


def create_tables():
    with db:
        db.create_tables([Recipe])


class Recipe(BaseModel):
    recipe_id = peewee.AutoField()
    cost = peewee.DecimalField()
    menu = peewee.ForeignKeyField(Menu, field="menu_id")
    ingredient = peewee.ForeignKeyField(Ingredient, field="ingredient_id")

    def __init__(self, cost: int | float, menu: int, ingredient: int) -> None:
        super().__init__()
        self.cost = cost
        self.menu = menu
        self.ingredient = ingredient
        Recipe.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'cost': r'^(^\d{1,10}\.\d{1,5}$)|(^\d{1,10}$)$',
            'menu': r'^\d{1,10}$',
            'ingredient': r'^\d{1,10}$'
        }

        messages = [
            'max 10 digits and 5 decimal places',
            'max 10 digits',
            'max 10 digits'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1


# create_tables()
