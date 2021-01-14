from typing import List


class OfficeEquipment:
    def __init__(self, serial_number: str, name: str):
        self._serial_number = serial_number
        self._name = name

    @property
    def name(self):
        return self._name


class Printer(OfficeEquipment):
    def __init__(self, serial_number: str, name: str, model: str, color_palette: []):
        super().__init__(serial_number, name)
        self._model = model
        self._color_palette = color_palette


class Scanner(OfficeEquipment):
    def __init__(self, serial_number: str, name: str, scan_format: str):
        super().__init__(serial_number, name)
        self._scan_format = scan_format


class Xerox(OfficeEquipment):
    def __init__(self, serial_number: str, name: str, copy_limit_per_day: int):
        super().__init__(serial_number, name)
        self._copy_limit_per_day = copy_limit_per_day


class OfficeWarehouse:
    def __init__(self, office_equipment: List[OfficeEquipment] = None):
        self._office_equipment_list = office_equipment if office_equipment else []

    def append(self, equipment: OfficeEquipment) -> None:
        self._office_equipment_list.append(equipment)
