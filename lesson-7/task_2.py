from abc import ABC, abstractmethod


class AbstractClothes(ABC):
    def __init__(self, name: str, size: float, height: float):
        self.__name = name
        self.__size = size
        self.__height = height

    @property
    def name(self) -> str:
        return self.__name

    @property
    def size(self) -> float:
        return self.__size

    @size.setter
    def size(self, value: float):
        self.__size = value

    @property
    def height(self) -> float:
        return self.__height

    @height.setter
    def height(self, value: float):
        self.__height = value

    @abstractmethod
    def calc_tissue_consumption(self) -> float:
        pass


class Coat(AbstractClothes):
    def calc_tissue_consumption(self) -> float:
        return self.size / 6.5 + 0.5


class Costume(AbstractClothes):
    def calc_tissue_consumption(self) -> float:
        return self.height * 2.0 + 0.3


coat = Coat('Coat', 50, 80)
costume = Costume('Costume', 50, 80)

print('{0:<.3f}'.format(coat.calc_tissue_consumption()))
print('{0:<.3f}'.format(costume.calc_tissue_consumption()))

clothes = [coat, costume]
print('{0:<.3f}'.format(sum(map(lambda c: c.calc_tissue_consumption(), clothes))))
