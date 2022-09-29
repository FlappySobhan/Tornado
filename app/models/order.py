import re
import peewee
from datetime import datetime

from models.base import BaseModel
from models.user import Users
from models.desk import Desk
from models.status import Status
from models.coupon import Coupon
from core.exceptions import StructureError


class Order(BaseModel):
    id = peewee.AutoField()
    register = peewee.DateTimeField(datetime.now())
    deliver = peewee.CharField()
    code = peewee.CharField()
    cost = peewee.DecimalField()
    user = peewee.ForeignKeyField(Users, field="id")
    desk = peewee.ForeignKeyField(Desk, field="id")
    status = peewee.ForeignKeyField(Status, field="id")
    coupon = peewee.ForeignKeyField(Coupon, field="id")

    def __init__(self, deliver: str, code: int, cost: int | float, user: int,
                 desk: int, status: int, coupon: int) -> None:
        super().__init__()
        self.deliver = deliver
        self.code = code
        self.cost = cost
        self.user = user
        self.desk = desk
        self.status = status
        self.coupon = coupon
        Order.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'deliver': r'^([0-5][0-9][0-9][0-9])-(([0][0-9])|[1][0-2])-(([0][0-9])|([1][0-9])|([2][0-9])|([3][0-1])) '
                       r'([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])$',
            'code': r'^\d{1,5}$',
            'cost': r'(^\d{1,10}\.\d{1,5}$)|(^\d{1,10}$)',
            'user': r'^\d{1,10}$',
            'desk': r'^\d{1,10}$',
            'status': r'^\d{1,10}$',
            'coupon': r'^\d{1,10}$'
        }

        messages = [
            'yyyy-mm-dd hh:mm:ss',
            'numeric max 5 digits',
            'max 10 digits and 5 decimal places',
            'max 10 digits',
            'max 10 digits',
            'max 10 digits',
            'max 10 digits'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
