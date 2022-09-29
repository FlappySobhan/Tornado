import re
import peewee

from models.base import BaseModel
from core.exceptions import StructureError


class Rule(BaseModel):
    id = peewee.AutoField()
    rule = peewee.CharField()

    def __init__(self, rule: str) -> None:
        super().__init__()
        self.rule = rule
        Rule.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'rule': r'^(customer|employee|admin)$'
        }

        messages = [
            'customer OR employee OR admin'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
