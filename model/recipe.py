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
            'cost': r'^[1-9]\d*(\.\d+)?$'
        }

        messages = [
            'integer or decimal number'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
