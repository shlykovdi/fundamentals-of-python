numbers = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
print(numbers)
non_recurring_numbers = [value for value in numbers if numbers.count(value) == 1]
print(non_recurring_numbers)
