import re
import peewee

from model.configs import db
from model.configs import BaseModel
from exceptions import StructureError


def create_tables():
    with db:
        db.create_tables([Menu])


class Menu(BaseModel):
    id = peewee.PrimaryKeyField()
    name = peewee.CharField()
    price = peewee.DecimalField()
    discount = peewee.DecimalField()
    category = peewee.CharField()
    meal = peewee.CharField()
    preparation = peewee.TimeField()

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

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'name': r'^([a-zA-Z]+[a-zA-Z\- ]*[a-zA-Z]+){2,30}$',
            'price': r'(^\d{1,10}\.\d{1,5}$)|(^\d{1,10}$)',
            'discount': r'(^\d{1,5}\.\d{1,5}$)|(^\d{1,5}$)',
            'category': r'^.{1,50}$',
            'meal': r'^.{1,50}$',
            'preparation': r'^([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])$'
        }

        messages = [
            'alphabetic 2~30 char',
            'max 10 digits and 5 decimal places',
            'max 10 digits and 5 decimal places',
            'max 50 char',
            'max 50 char',
            'hh:mm:ss'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1


create_tables()
