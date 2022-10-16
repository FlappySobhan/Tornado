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
    created_at = peewee.DateTimeField(default=datetime.now())
    user = peewee.ForeignKeyField(Users, field="id", null=True)

    def __init__(self, name: str, email: str, message: str, user: int | None = None, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.name = name
        self.email = email
        self.message = message
        self.user = user

        # if we are in registering new data then validate the fields
        if not kwargs.get('id'):
            Contact.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'created_at': r'.',
            'name': r'((^[\u0600-\u06F0]{2,30}$)|(^[\u0600-\u06F0]{2,15}[ ][\u0600-\u06F0]{2,15}$))|((^[A-Za-z]{2,'
                    r'30}$)|(^[A-Za-z]{2,15}[ ][A-Za-z]{2,15}$))',
            'email': r'^[\w|.|-]+@\w*\.[\w|.]*$',
            'message': r'.',
            'user': r'^\d{1,10}|None$',
            'id': r'^\d{1,}$'
        }

        messages = [
            'auto fill',
            'alphabetic 2~30 char',
            'standard email format',
            'should be not empty',
            'empty or max 10 digits',
            'auto filled'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
