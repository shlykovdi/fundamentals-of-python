class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def calc_weight(self):
        return self._length * self._width * 25 * 15


road = Road(15000, 20)
print(f'Road weight: {road.calc_weight()} tons')
