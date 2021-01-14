from datetime import datetime
from typing import Union


class Date:
    date: str = ''

    def __init__(self, date: str):
        Date.date = date

    @classmethod
    def extract(cls) -> Union[tuple, None]:
        try:
            date = datetime.strptime(cls.date, '%d-%m-%Y')  # life hack
        except ValueError:
            return None
        return date.day, date.month, date.year

    @staticmethod
    def validate() -> bool:
        result = Date.extract()
        if not result:
            return False
        day, month, year = result
        return (1 <= day <= 31) and (1 <= month <= 12) and (1 <= year <= 9999)  # this will don't work correctly all time :)


print(Date('15-08-2021').extract())
print(Date('15-08-2021').validate())

print(Date('150-08-2021').extract())
print(Date('15-80-2021').validate())
