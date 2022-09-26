import re
import peewee

from model.configs import BaseModel
from core.exceptions import StructureError


class Desk(BaseModel):
    """Desk table definition and validation"""
    desk_id = peewee.AutoField()
    number = peewee.IntegerField()
    capacity = peewee.IntegerField()
    status = peewee.CharField()
    cost = peewee.DecimalField()

    def __init__(self, name: str, number: int, capacity: int, status: str, cost: int | float) -> None:
        super().__init__()
        self.name = name
        self.number = number
        self.capacity = capacity
        self.status = status
        self.cost = cost
        Desk.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'name': r'^([a-zA-Z]+[a-zA-Z\- ]*[a-zA-Z]+){2,25}$',
            'number': r'^\d{1,3}$',
            'capacity': r'^\d{1,2}$',
            'status': r'^.{1,250}$',
            'cost': r'(^\d{1,10}\.\d{1,5}$)|(^\d{1,10}$)'
        }

        messages = [
            'name 2~25 char',
            'numeric max 3 digits',
            'numeric max 2 digits',
            'max 250 char',
            'max 10 digits and 5 decimal places'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
