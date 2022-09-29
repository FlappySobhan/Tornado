import re
import peewee
from datetime import datetime

from models.base import BaseModel
from models.user import Users
from core.exceptions import StructureError


class Contact(BaseModel):
    id = peewee.AutoField()
    name = peewee.CharField()
    email = peewee.CharField()
    message = peewee.TextField()
    created_at = peewee.DateTimeField(datetime.now())
    user = peewee.ForeignKeyField(Users, field="id", null=True)

    def __init__(self, name: str, email: str, message: str, user: int = None) -> None:
        super().__init__()
        self.name = name
        self.email = email
        self.message = message
        self.user = user
        Contact.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'name': r'^([a-zA-Z]+[a-zA-Z\- ]*[a-zA-Z]+){2,25}$',
            'email': r'^[\w|.|-]+@\w*\.[\w|.]*$',
            'message': r'.',
            'user': r'^\d{1,10}|$'
        }

        messages = [
            'alphabetic 2~25 char',
            'standard email format',
            'unlimited',
            'empty or max 10 digits'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
