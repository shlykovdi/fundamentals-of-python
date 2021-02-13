import sys


class MyZeroDivisionError(ZeroDivisionError):
    pass


try:
    a = int(input('Enter number A: '))
    b = int(input('Enter number B: '))
except ValueError as error:
    print(error)
    sys.exit(-1)


def calc_div(value_a: int, value_b: int) -> int:
    if not value_b:
        raise MyZeroDivisionError('Zero division!')
    return value_a // value_b


try:
    print(f'Result a // b = {calc_div(a, b)}')
except MyZeroDivisionError as error:
    print(error)
