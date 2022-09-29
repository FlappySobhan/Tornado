import re
import peewee

from models.base import BaseModel
from models.category import Category
from core.exceptions import StructureError


class Menu(BaseModel):
    id = peewee.AutoField()
    name = peewee.CharField()
    price = peewee.DecimalField()
    discount = peewee.DecimalField()
    preparation = peewee.TimeField()
    category = peewee.ForeignKeyField(Category, field="id")

    def __init__(self, name: str, price: int | float, discount: int | float,
                 preparation: str, category: int) -> None:

        super().__init__()
        self.name = name
        self.price = price
        self.discount = discount
        self.preparation = preparation
        self.category = category
        Menu.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'name': r'^([a-zA-Z]+[a-zA-Z\- ]*[a-zA-Z]+){2,30}$',
            'price': r'(^\d{1,10}\.\d{1,5}$)|(^\d{1,10}$)',
            'discount': r'(^\d{1,5}\.\d{1,5}$)|(^\d{1,5}$)',
            'preparation': r'^([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])$',
            'category': r'^\d{1,10}$'
        }

        messages = [
            'alphabetic 2~30 char',
            'max 10 digits and 5 decimal places',
            'max 10 digits and 5 decimal places',
            'hh:mm:ss',
            'max 10 digits'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
