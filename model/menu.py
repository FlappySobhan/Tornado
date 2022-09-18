import re
from peewee import *

from model.configs import db
from model.configs import BaseModel
from exceptions import StructureError


def create_tables():
    with db:
        db.create_tables([Menu])


class Menu(BaseModel):

    id = PrimaryKeyField()
    name = CharField()
    price = DecimalField()
    discount = DecimalField()
    category = CharField()
    meal = CharField()
    preparation = TimeField()

    def __init__(self, name: str, price: int | float, discount: int | float,
                 category: str, meal: str, preparation: str) -> None:

        super().__init__()
        self.name = name
        self.price = price
        self.discount = discount
        self.category = category
        self.meal = meal
        self.preparation = preparation
        Menu.validation(self.__dict__['__data__'])
        self.save(self)

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'name': r'^([a-zA-Z]+[a-zA-Z\- ]*[a-zA-Z]+){2,30}$',
            'price': r'^[1-9]\d*(\.\d+)?$',
            'discount': r'^[1-9]\d*(\.\d+)?$',
            'category': r'^.{1,50}$',
            'meal': r'^.{1,50}$',
            'preparation': r'^.{1,50}$'
        }

        messages = [
            'alphabetic 2~30 char',
            'integer or decimal number',
            'integer or decimal number',
            'max 50 char',
            'max 50 char',
            'max 50 char'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
