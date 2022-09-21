import re
import peewee

from model.configs import db
from model.configs import BaseModel
from model.order import Order
from exceptions import StructureError


def create_tables_receipts():
    with db:
        db.create_tables([Receipts])


class Receipts(BaseModel):
    receipts_id = peewee.AutoField()
    cost = peewee.DecimalField()
    delivery = peewee.TimestampField()
    code = peewee.IntegerField()
    customer = peewee.CharField()
    desk = peewee.IntegerField()
    order = peewee.ForeignKeyField(Order, field="order_id")

    def __init__(self, cost: int | float, delivery: str, code: int, customer: str, desk: int, order: int) -> None:
        super().__init__()
        self.cost = cost
        self.delivery = delivery
        self.code = code
        self.customer = customer
        self.desk = desk
        self.order = order
        Receipts.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'cost': r'^(^\d{1,10}\.\d{1,5}$)|(^\d{1,10}$)$',
            'delivery': r'^([0-5][0-9][0-9][0-9])-(([0][0-9])|[1][0-2])-(([0][0-9])|([1][0-9])|([2][0-9])|([3][0-1])) '
                        r'([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])$',
            'code': r'^\d{1,5}$',
            'customer': r'^([a-zA-Z]+[a-zA-Z\- ]*[a-zA-Z]+){2,50}$',
            'desk': r'^\d{1,3}$',
            'order': r'^\d{1,10}$'
        }

        messages = [
            'max 10 digits and 5 decimal places',
            'max 50 char',
            'numeric max 5 digits',
            'alphabetic 2~50 char',
            'numeric max 3 digits',
            'max 10 digits'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
