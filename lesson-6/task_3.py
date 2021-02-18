class Worker:
    def __init__(self, name, surname, position):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': 0, 'bonus': 0}


class Position(Worker):
    def __init__(self, name, surname, position):
        super().__init__(name, surname, position)

    @property
    def wage(self):
        return self._income['wage']

    @wage.setter
    def wage(self, value):
        self._income['wage'] = value

    @property
    def bonus(self):
        return self._income['bonus']

    @bonus.setter
    def bonus(self, value):
        self._income['bonus'] = value

    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        return self.wage + self.bonus


position = Position('Elon', 'Mask', 'Developer')
position.wage = 50000
position.bonus = 20000

print(position.get_full_name())
print(f'{position.get_total_income()}$')
