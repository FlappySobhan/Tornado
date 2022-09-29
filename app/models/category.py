import re
import peewee

from models.base import BaseModel
from core.exceptions import StructureError


class Category(BaseModel):
    """Desk table definition and validation"""

    id = peewee.AutoField()
    name = peewee.CharField()
    parent = peewee.CharField()
    relation = peewee.ForeignKeyField('self', field='id', null=True)

    def __init__(self, name: str, parent: str, relation: int = None) -> None:
        super().__init__()
        self.name = name
        self.parent = parent
        self.relation = relation
        Category.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'name': r'^([a-zA-Z]+[a-zA-Z\- ]*[a-zA-Z]+){2,25}$',
            'parent': r'^([a-zA-Z]+[a-zA-Z\- ]*[a-zA-Z]+){2,25}$',
            'relation': r'^\d{1,10}$'
        }

        messages = [
            'name 2~25 char',
            'name 2~25 char',
            'max 10 digits'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
