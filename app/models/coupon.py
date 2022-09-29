import re
import peewee

from models.base import BaseModel
from core.exceptions import StructureError


class Coupon(BaseModel):
    id = peewee.AutoField()
    code = peewee.CharField()
    amount = peewee.DecimalField()

    def __init__(self, code: str, amount: int | float) -> None:
        super().__init__()
        self.code = code
        self.amount = amount
        Coupon.validation(self.__dict__['__data__'])

    @staticmethod
    def validation(data: dict) -> None:
        """Regex validator"""

        patterns = {
            'code': r'^.{1,50}$',
            'amount': r'^(^\d{1,10}\.\d{1,5}$)|(^\d{1,10}$)$'
        }

        messages = [
            'max 50 char',
            'max 10 digits and 5 decimal places'
        ]

        counter = 0
        for key, value in data.items():
            if not re.match(patterns[key], str(value)):
                raise StructureError(key, messages[counter])
            counter += 1
