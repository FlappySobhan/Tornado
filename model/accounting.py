import re
import peewee

from model.configs import BaseModel
from model.order import Order
from exceptions import StructureError


class Accounting(BaseModel):
    accounting_id = peewee.AutoField()
    profit = peewee.DecimalField()
    description = peewee.CharField()
    order = peewee.ForeignKeyField(Order, field='order_id')

    def __init__(self, profit: int | float, description: str, order: int) -> None:
        super().__init__()
        self.profit = profit
        self.description = description
        self.order = order
        Accounting.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'profit': r'(^\d{1,10}\.\d{1,5}$)|(^\d{1,10}$)',
            'description': r'^.{1,250}$',
            'order': r'^\d{1,10}$'
        }

        messages = [
            'max 10 digits and 5 decimal places',
            'max 250 chars',
            'max 10 digits'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
