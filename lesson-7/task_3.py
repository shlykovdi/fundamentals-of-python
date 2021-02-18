class SubCellException(Exception):
    pass


class Cell:
    __slots__ = '__count'

    def __init__(self, count: int):
        self.__count = count

    @property
    def count(self) -> int:
        return self.__count

    def __add__(self, other):
        return Cell(self.count + other.count)

    def __sub__(self, other):
        if self.count - other.count < 0:
            raise SubCellException(f'{self.count - other.count} < 0. Subtraction is not possible!')
        return Cell(self.count - other.count)

    def __mul__(self, other):
        return Cell(self.count * other.count)

    def __truediv__(self, other):
        import math
        return Cell(math.floor(self.count / other.count))

    def make_order(self, count_in_row: int) -> str:
        string = ''
        count = self.count
        while count > 0:
            string += f'{"*" * min(count, count_in_row)}\n'
            count -= count_in_row
        return string


cell_1 = Cell(20)
cell_2 = Cell(25)
cell_3 = Cell(10)
cell_4 = Cell(10)
cell_5 = Cell(6)

print((cell_1 + cell_2).count)
print((cell_2 - cell_3).count)
print((cell_3 * cell_4).count)
print((cell_4 / cell_5).count)

print(cell_1.make_order(10))
print(cell_2.make_order(6))
print(cell_3.make_order(8))
print(cell_4.make_order(7))
print(cell_5.make_order(1))
