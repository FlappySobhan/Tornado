import re
import peewee

from models.base import BaseModel
from core.exceptions import StructureError


class Status(BaseModel):
    id = peewee.AutoField()
    status = peewee.CharField()

    def __init__(self, status: str) -> None:
        super().__init__()
        self.status = status
        Status.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'status': r'^(cooking|canceled|delivered|waiting)$'
        }

        messages = [
            'cooking OR canceled OR delivered OR waiting'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
