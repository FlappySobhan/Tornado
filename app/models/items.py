import re
import peewee

from models.base import BaseModel
from models.menu import Menu
from models.order import Order
from core.exceptions import StructureError


class Items(BaseModel):
    id = peewee.AutoField()
    menu = peewee.ForeignKeyField(Menu, field="id")
    order = peewee.ForeignKeyField(Order, field="id")

    def __init__(self, menu: int, order: int) -> None:
        super().__init__()
        self.menu = menu
        self.order = order
        Items.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'menu': r'^\d{1,10}$',
            'order': r'^\d{1,10}$'
        }

        messages = [
            'max 10 digits',
            'max 10 digits'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
