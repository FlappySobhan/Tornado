import re
import peewee
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

from models.base import BaseModel
from models.rule import Rule
from core.exceptions import StructureError


class Users(BaseModel, UserMixin):
    id = peewee.AutoField()
    name = peewee.CharField()
    family = peewee.CharField()
    phone = peewee.CharField(unique=True)
    address = peewee.CharField()
    password = peewee.CharField()
    balance = peewee.DecimalField()
    subscription = peewee.CharField()
    created_at = peewee.DateTimeField(default=datetime.now())
    rule = peewee.ForeignKeyField(Rule, field="id")

    def __init__(self, name: str, family: str, phone: str, address: str, password: str,
                 balance: int | float, subscription: int, rule: int, *args, **kwargs) -> None:

        super().__init__(*args, **kwargs)
        self.name = name
        self.family = family
        self.phone = phone
        self.address = address
        self.password = password
        self.balance = balance
        self.subscription = subscription
        self.rule = rule

        # if we are in registering new data then validate the fields
        if not kwargs.get('id'):
            Users.validation(self.__dict__['__data__'])
            self.password = generate_password_hash(self.password, method="pbkdf2:sha256")

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'created_at': r'.*',
            'name': r'((^[\u0600-\u06F0]{2,30}$)|(^[\u0600-\u06F0]{2,15}[ ][\u0600-\u06F0]{2,15}$))|((^[A-Za-z]{2,'
                    r'30}$)|(^[A-Za-z]{2,15}[ ][A-Za-z]{2,15}$))',
            'family': r'((^[\u0600-\u06F0]{2,30}$)|(^[\u0600-\u06F0]{2,15}[ ][\u0600-\u06F0]{2,15}$))|((^[A-Za-z]{2,'
                    r'30}$)|(^[A-Za-z]{2,15}[ ][A-Za-z]{2,15}$))',
            'phone': r'^(0|\+98)?[1-9]+[\d]{9}$',
            'address': r'^.{1,250}$',
            'password': r'^(?=.*\d)(?=.*[a-z])(?=.*[a-zA-Z]).{8,40}$',
            'balance': r'^\d+(\.\d+)?$',
            'subscription': r'^\d{1,8}$',
            'rule': r'^\d{1,10}$',
            'id': r'^\d{1,}$'
        }

        messages = [
            'auto filled',
            'alphabetic 2~30 char',
            'alphabetic 2~30 char',
            'numeric, 10 primary digits',
            'max 250 char',
            'complex with 8~40 char',
            'numeric max 10 digits',
            'numeric max 8 digits',
            'max 10 digits',
            'auto filled'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
