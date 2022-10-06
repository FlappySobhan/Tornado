import re
import peewee

from models.base import BaseModel
from models.menu import Menu
from models.ingredient import Ingredient
from core.exceptions import StructureError


class Recipe(BaseModel):
    """Recipe table definition and validation"""

    id = peewee.AutoField()
    quantity = peewee.DecimalField()
    menu = peewee.ForeignKeyField(Menu, field="id")
    ingredient = peewee.ForeignKeyField(Ingredient, field="id")

    def __init__(self, quantity: int | float, menu: int, ingredient: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.quantity = quantity
        self.menu = menu
        self.ingredient = ingredient

        # if we are in registering new data then validate the fields
        if not kwargs.get('id'):
            Recipe.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'quantity': r'^(^\d{1,10}\.\d{1,5}$)|(^\d{1,10}$)$',
            'menu': r'^\d{1,10}$',
            'ingredient': r'^\d{1,10}$',
            'id': r'^\d{1,}$'
        }

        messages = [
            'max 10 digits and 5 decimal places',
            'max 10 digits',
            'max 10 digits',
            'auto filled'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
