import re
import peewee
from datetime import datetime

from model.configs import db
from model.configs import BaseModel
from exceptions import StructureError


def create_tables():
    with db:
        db.create_tables([Users])


class Users(BaseModel):
    user_id = peewee.AutoField()
    name = peewee.CharField()
    family = peewee.CharField()
    phone = peewee.CharField()
    address = peewee.CharField()
    password = peewee.CharField()
    balance = peewee.DecimalField()
    privilege = peewee.CharField()
    subscription = peewee.CharField()
    created_at = peewee.DateTimeField(datetime.now())

    def __init__(self, name: str, family: str, phone: str, address: str, password: str,
                 balance: int | float, subscription: int, privilege: str = 'public') -> None:

        super().__init__()
        self.name = name
        self.family = family
        self.phone = phone
        self.address = address
        self.password = password
        self.balance = balance
        self.subscription = subscription
        self.privilege = privilege
        Users.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'name': r'^([a-zA-Z]+[a-zA-Z\- ]*[a-zA-Z]+){2,25}$',
            'family': r'^([a-zA-Z]+[a-zA-Z\- ]*[a-zA-Z]+){2,25}$',
            'phone': r'^(0|\+98)?[1-9]+[\d]{9}$',
            'address': r'^.{1,250}$',
            'password': r'^(?=.*\d)(?=.*[a-z])(?=.*[a-zA-Z]).{8,40}$',
            'balance': r'^[1-9]\d*(\.\d+)?$',
            'subscription': r'^\d{1,8}$',
            'privilege': r'^.{1,40}$'
        }

        messages = [
            'alphabetic 2~25 char',
            'alphabetic 2~25 char',
            'numeric, 10 primary digits',
            'max 250 char',
            'complex with 8~40 char',
            'numeric max 10 digits',
            'numeric max 8 digits',
            'max 40 chars'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1


# create_tables()
