import re
import peewee

from models.base import BaseModel
from core.exceptions import StructureError


class Rule(BaseModel):
    id = peewee.AutoField()
    rule = peewee.CharField()

    def __init__(self, rule: str, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.rule = rule

        # if we are in registering new data then validate the fields
        if not kwargs.get('id'):
            Rule.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'rule': r'^(مشتری|کارمند|ادمین)$',
            'id': r'^\d{1,}$'
        }

        messages = [
            'customer OR employee OR admin',
            'auto filled'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
