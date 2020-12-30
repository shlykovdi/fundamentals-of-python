from typing import Iterable, TypeVar, Generic


T = TypeVar('T', int, float)


class MatrixDiffSizesException(Exception):
    pass


class Matrix(Generic[T]):
    def __init__(self, matrix: Iterable[Iterable[T]]):
        self.data = [[column for column in row] for row in matrix]

    def __str__(self) -> str:
        string = ''
        for row in self.data:
            for column in row:
                string += f'{column},\t'
            string += '\n'
        return string

    def size(self) -> (int, int):
        rows = len(self.data)
        return rows, len(self.data[0]) if rows else 0

    def __add__(self, other):
        if self.size() != other.size():
            raise MatrixDiffSizesException(f'{self.size()} != {other.size()}')
        return Matrix([[c_self + c_other for c_self, c_other in zip(r_self, r_other)] for r_self, r_other in zip(self.data, other.data)])


m1 = Matrix([[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]])

m2 = Matrix([[1, 2, 3, 4],
             [5, 6, 7, 8],
             [9, 10, 11, 12],
             [13, 14, 15, 16]])

print(m1.size())
print(m1)
print(m2.size())
print(m2)
print(m1 + m2)
