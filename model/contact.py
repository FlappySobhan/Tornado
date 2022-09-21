import re
import peewee
from datetime import datetime

from model.configs import db
from model.configs import BaseModel
from exceptions import StructureError


def create_tables_contact():
    with db:
        db.create_tables([Contact])


class Contact(BaseModel):
    contact_id = peewee.AutoField()
    name = peewee.CharField()
    email = peewee.CharField()
    message = peewee.TextField()
    created_at = peewee.DateTimeField(datetime.now())

    def __init__(self, name: str, email: str, message: str) -> None:
        super().__init__()
        self.name = name
        self.email = email
        self.message = message
        Contact.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'name': r'^([a-zA-Z]+[a-zA-Z\- ]*[a-zA-Z]+){2,25}$',
            'email': r'^[\w|.|-]+@\w*\.[\w|.]*$',
            'message' : r'.',
        }

        messages = [
            'alphabetic 2~25 char',
            'standard email format',
            'unlimited',
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
