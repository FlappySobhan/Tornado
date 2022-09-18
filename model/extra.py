import re
from peewee import *

from model.configs import db
from model.configs import BaseModel
from model.user import Users
from exceptions import StructureError


def create_tables():
    with db:
        db.create_tables([Extra])


class Extra(BaseModel):

    id = PrimaryKeyField()
    email = CharField()
    phone = CharField()
    address = CharField()
    info = TextField()
    user_id = ForeignKeyField(Users, to_field="id")

    def __init__(self, email: str, phone: str, address: str, info: str) -> None:
        super().__init__()
        self.email = email
        self.phone = phone
        self.address = address
        self.info = info
        Extra.validation(self.__dict__['__data__'])
        self.save(self)

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'email': r'[\w|.|-]*@\w*\.[\w|.]*',
            'phone': r'^(0|\+98)?[1-9]+[\d]{9}$',
            'address': r'^.{1,250}$',
            'info': r'.'
        }

        messages = [
            'standard email format',
            'numeric, 10 primary digits',
            'max 250 char',
            'unlimited'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
