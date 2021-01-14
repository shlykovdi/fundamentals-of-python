from typing import (Type, Callable)
from random import randint

from task_4 import (OfficeWarehouse, OfficeEquipment, Printer, Scanner, Xerox)


class Company:
    def __init__(self):
        self.office_warehouse = OfficeWarehouse()
        self.subdivisions = {}

    def append_equipment(self, subdivisions: str, equipment: OfficeEquipment) -> None:
        self.office_warehouse.append(equipment)
        subdivision_data = self.subdivisions.get(subdivisions)
        if subdivision_data:
            subdivision_data[1].append(equipment.name)
            subdivision_data[0] = len(subdivision_data[1])
        else:
            self.subdivisions[subdivisions] = [1, [equipment.name]]

    def print_subdivisions(self) -> None:
        print(self.subdivisions)


def run(company_class: Type[Company], get_equipment_count: Callable[[], int]) -> None:
    company = company_class()

    company.append_equipment('Python Dev', Printer('123325NSD5', 'Printer', 'HP', [0, 1, 2, 3, 4, 5]))
    company.append_equipment('Python Dev', Scanner('897324QWE', 'Scanner', 'super puper format'))

    company.append_equipment('DevOps', Scanner('897324QWE', 'Scanner', 'super puper format'))
    company.append_equipment('DevOps', Xerox('KJHLM3213LBGV', 'Xerox', 666))

    for _ in range(get_equipment_count()):
        if randint(0, 1):
            company.append_equipment('Bookkeeping', Scanner('897324QWE', 'Scanner', 'super puper format'))
        else:
            company.append_equipment('Bookkeeping', Printer('123325NSD5', 'Printer', 'HP', [0, 1, 2, 3, 4, 5]))

    company.print_subdivisions()

if __name__ == '__main__':
    run(Company, lambda: 8)
