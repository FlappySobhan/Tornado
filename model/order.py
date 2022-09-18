import re
from peewee import *
from configs import db
from configs import BaseModel

from model.user import Users
from model.menu import Menu
from model.desk import Desk
from exceptions import StructureError


def create_tables():
    with db:
        db.create_tables([Order])


class Order(BaseModel):
    id = PrimaryKeyField()
    status = CharField()
    register = CharField()
    deliver = CharField()
    code = CharField()
    cost = CharField()
    user_id = ForeignKeyField(Users, to_field="id")
    menu_id = ForeignKeyField(Menu, to_field="id")
    desk_id = ForeignKeyField(Desk, to_field="id")

    def __init__(self, status: str, register: str, deliver: str, code: int, cost: int | float) -> None:
        super().__init__()
        self.status = status
        self.register = register
        self.deliver = deliver
        self.code = code
        self.cost = cost
        Order.validation(self.__dict__['__data__'])
        self.save(self)

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'status': r'^.{1,50}$',
            # timestamp regex yyyy-mm-dd hh:mm:ss
            'register': r'^([0-5][0-9][0-9][0-9])-(([0][0-9])|[1][0-2])-(([0][0-9])|([1][0-9])|([2][0-9])|([3][0-1])) '
                        r'([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])$',
            # timestamp regex yyyy-mm-dd hh:mm:ss
            'deliver': r'^([0-5][0-9][0-9][0-9])-(([0][0-9])|[1][0-2])-(([0][0-9])|([1][0-9])|([2][0-9])|([3][0-1])) '
                       r'([0-1][0-9]|[2][0-3]):([0-5][0-9]):([0-5][0-9])$',
            'code': r'^\d{1,5}$',
            'cost': r'(^\d{1,10}\.\d{1,5}$)|(^\d{1,10}$)'
        }

        messages = [
            'max 50 char',
            'max 50 char',
            'max 50 char',
            'numeric max 5 digits',
            'integer or decimal number and maximum 5 digits'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
