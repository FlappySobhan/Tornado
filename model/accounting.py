import re
from peewee import *

from model.configs import db
from model.configs import BaseModel
from model.order import Order
from exceptions import StructureError


def create_tables():
    with db:
        db.create_tables([Accounting])


class Accounting(BaseModel):

    id = PrimaryKeyField()
    profit = CharField()
    description = CharField()
    order_id = ForeignKeyField(Order, to_field="id")

    def __init__(self, profit: int | float, description: str) -> None:
        super().__init__()
        self.profit = profit
        self.description = description
        Accounting.validation(self.__dict__['__data__'])
        self.save(self)

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'profit': r'^[1-9]\d*(\.\d+)?$',
            'description': r'^.{1,250}$'
        }

        messages = [
            'integer or decimal number',
            'max 250 chars'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
