from __future__ import annotations


class Complex:
    __slots__ = 'real', 'imag'

    def __init__(self, real: float = 0.0, imag: float = 0.0):
        self.real = real
        self.imag = imag

    def __add__(self, other: Complex) -> Complex:
        return Complex(self.real + other.real, self.imag + other.imag)

    def __mul__(self, other: Complex) -> Complex:
        return Complex(self.real * other.real - self.imag * other.imag, self.real * other.imag + other.real * self.imag)

    def __str__(self) -> str:
        return f'({self.real}{"+" if self.imag >= 0.0 else "-"}{abs(self.imag)}j)'


def run() -> None:
    my_c1 = Complex(5.0, 8.0)
    my_c2 = Complex(10.5, -12.5)

    sys_c1 = complex(5.0, 8.0)
    sys_c2 = complex(10.5, -12.5)

    print(my_c1 + my_c2)
    print(sys_c1 + sys_c2)

    print(my_c1 * my_c2)
    print(sys_c1 * sys_c2)


if __name__ == '__main__':
    run()
