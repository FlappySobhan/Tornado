import re
import peewee
from datetime import datetime
from werkzeug.security import generate_password_hash

from models.base import BaseModel
from models.rule import Rule
from core.exceptions import StructureError


class Users(BaseModel):
    id = peewee.AutoField()
    name = peewee.CharField()
    family = peewee.CharField()
    phone = peewee.CharField()
    address = peewee.CharField()
    password = peewee.CharField()
    balance = peewee.DecimalField()
    subscription = peewee.CharField()
    created_at = peewee.DateTimeField(default=datetime.now())
    rule = peewee.ForeignKeyField(Rule, field="id")

    def __init__(self, name: str, family: str, phone: str, address: str, password: str,
                 balance: int | float, subscription: int, rule: int = 1) -> None:

        super().__init__()
        self.name = name
        self.family = family
        self.phone = phone
        self.address = address
        self.password = password
        self.balance = balance
        self.subscription = subscription
        self.rule = rule
        Users.validation(self.__dict__['__data__'])
        self.password = generate_password_hash(self.password, method="pbkdf2:sha256")

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
            'created_at': r'.*',
            'rule': r'^\d{1,10}$'
        }

        messages = [
            'alphabetic 2~25 char',
            'alphabetic 2~25 char',
            'numeric, 10 primary digits',
            'max 250 char',
            'complex with 8~40 char',
            'numeric max 10 digits',
            'numeric max 8 digits',
            'auto filled',
            'max 10 digits'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
