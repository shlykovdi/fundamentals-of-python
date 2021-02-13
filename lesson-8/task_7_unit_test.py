import unittest

from task_7 import Complex
from random import uniform


class ComplexNumbersTest(unittest.TestCase):
    @staticmethod
    def rand() -> float:
        return uniform(-50.0, 50.0)

    def test_add(self):
        for _ in range(100000):
            real1, imag1 = self.rand(), self.rand()
            real2, imag2 = self.rand(), self.rand()
            my_c = Complex(real1, imag1) + Complex(real2, imag2)
            sys_c = complex(real1, imag1) + complex(real2, imag2)
            self.assertEqual(my_c.real, sys_c.real)
            self.assertEqual(my_c.imag, sys_c.imag)

    def test_mul(self):
        for _ in range(100000):
            real1, imag1 = self.rand(), self.rand()
            real2, imag2 = self.rand(), self.rand()
            my_c = Complex(real1, imag1) * Complex(real2, imag2)
            sys_c = complex(real1, imag1) * complex(real2, imag2)
            self.assertEqual(my_c.real, sys_c.real)
            self.assertEqual(my_c.imag, sys_c.imag)

    def test_str(self):
        for _ in range(100000):
            real1, imag1 = self.rand(), self.rand()
            real2, imag2 = self.rand(), self.rand()
            my_c = Complex(real1, imag1) + Complex(real2, imag2)
            sys_c = complex(real1, imag1) + complex(real2, imag2)
            self.assertEqual(my_c.__str__(), sys_c.__str__())

            real1, imag1 = self.rand(), self.rand()
            real2, imag2 = self.rand(), self.rand()
            my_c = Complex(real1, imag1) * Complex(real2, imag2)
            sys_c = complex(real1, imag1) * complex(real2, imag2)
            self.assertEqual(my_c.__str__(), sys_c.__str__())


if __name__ == '__main__':
    unittest.main()
