import functools


numbers = [value for value in range(100, 105) if not (value % 2)]
print(numbers)
print(f'Multiplication = {functools.reduce(lambda a, b: a * b, numbers)}')
