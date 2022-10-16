import re
import peewee

from models.base import BaseModel
from core.exceptions import StructureError


class Status(BaseModel):
    id = peewee.AutoField()
    status = peewee.CharField()

    def __init__(self, status: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.status = status

        # if we are in registering new data then validate the fields
        if not kwargs.get('id'):
            Status.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'status': r'^(در حال آماده‌سازی|لغو شده|تحویل داده شده|در صف انتظار)$',
            'id': r'^\d{1,}$'
        }

        messages = [
            'cooking OR canceled OR delivered OR waiting',
            'auto filled'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
