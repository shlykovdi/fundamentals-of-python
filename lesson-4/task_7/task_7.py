def factorial(number):
    for value in range(1, number + 1):
        yield value


for value in factorial(4):
    print(value)
