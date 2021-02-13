numbers = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
print(numbers)
bigger_numbers = [value for index, value in enumerate(numbers) if index and value > numbers[index - 1]]
print(bigger_numbers)
