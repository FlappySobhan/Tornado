import re
import peewee

from models.base import BaseModel
from models.user import Users
from core.exceptions import StructureError


class Extra(BaseModel):
    id = peewee.AutoField()
    email = peewee.CharField(null=True)
    phone = peewee.CharField(null=True)
    address = peewee.CharField(null=True)
    info = peewee.TextField(null=True)
    user = peewee.ForeignKeyField(Users, field="id")

    def __init__(self, email: str, phone: str, address: str, info: str, user: int, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.email = email
        self.phone = phone
        self.address = address
        self.info = info
        self.user = user

        # if we are in registering new data then validate the fields
        if not kwargs.get('id'):
            Extra.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'email': r'^[\w|.|-]+@\w*\.[\w|.]*$',
            'phone': r'^(0|\+98)?[1-9]+[\d]{9}$',
            'address': r'^.{1,250}$',
            'info': r'.*',
            'user': r'^\d{1,10}$',
            'id': r'^\d{1,}$'
        }

        messages = [
            'standard email format',
            'numeric, 10 primary digits',
            'max 250 char',
            'unlimited',
            'max 10 digits',
            'auto filled'
        ]

        counter = 0
        for key, value in data.items():
            if value and not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
