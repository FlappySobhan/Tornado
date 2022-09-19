import re
from peewee import *

from model.configs import db
from model.configs import BaseModel
from exceptions import StructureError


def create_tables():
    with db:
        db.create_tables([Ingredient])


class Ingredient(BaseModel):

    name = CharField()
    quantity = IntegerField()
    unit = CharField()
    category = CharField()
    cost = DecimalField()

    def __init__(self, name: str, quantity: int | float, unit: str, category: str, cost: int | float) -> None:
        super().__init__()
        self.name = name
        self.quantity = quantity
        self.unit = unit
        self.category = category
        self.cost = cost
        Ingredient.validation(self.__dict__['__data__'])
        self.save(self)

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'name': r'^([a-zA-Z]+[a-zA-Z\- ]*[a-zA-Z]+){2,30}$',
            'quantity': r'^\d{1,10}$',
            'unit': r'^.{1,40}$',
            'category': r'^.{1,40}$',
            'cost': r'(^\d{1,10}\.\d{1,5}$)|(^\d{1,10}$)'
        }

        messages = [
            'alphabetic 2~30 char',
            'numeric max 10 digits',
            'max 40 chars',
            'max 40 chars',
            'max 10 digits and 5 decimal places'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1


create_tables()
