import re
from peewee import *
from configs import db
from configs import BaseModel

from model.menu import Menu
from model.ingredient import Ingredient
from exceptions import StructureError


def create_tables():
    with db:
        db.create_tables([Recipe])


class Recipe(BaseModel):
    id = PrimaryKeyField()
    cost = DecimalField()
    menu_id = ForeignKeyField(Menu, to_field="id")
    material_id = ForeignKeyField(Ingredient, to_field="id")

    def __init__(self, cost: int | float) -> None:
        super().__init__()
        self.cost = cost
        Recipe.validation(self.__dict__['__data__'])
        self.save(self)

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'cost': r'(^\d{1,10}\.\d{1,5}$)|(^\d{1,10}$)'
        }

        messages = [
            'max 10 digits and 5 decimal places'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
