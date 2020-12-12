def func_name(func):
    def decorator(*args, **kwargs):
        print(f'>> {func.__name__.capitalize().replace("_", "-")}:')
        func(*args, **kwargs)
        print('')
    return decorator


@func_name
def task_1():
    list_types = [1, 'string', [{1, 2, 3}], {8}, ('abc', 456.789), {'key': 'value'}, bytes(range(0, 255)),
                  bytearray(range(0, 255)), 1.618, True, (i for i in range(8)), None, range(0),
                  complex(123.456, 789.123), Ellipsis, func_name]
    for element in list_types:
        print(type(element))


@func_name
def task_2():
    import itertools
    amount_of_elements = int(input('Enter the number of list elements: '))
    numbers = [int(input(f'Enter value {value}: ')) for value in range(amount_of_elements)]
    print(numbers)
    sliced_numbers = itertools.zip_longest(numbers[0::2], numbers[1::2])
    numbers.clear()
    for value0, value1 in sliced_numbers:
        if value1 is not None:
            numbers.append(value1)
        if value0 is not None:
            numbers.append(value0)
    print(numbers)


@func_name
def task_3():
    months_dict_info = {12: 'Winter', 1: 'Winter', 2: 'Winter',
                        3: 'Spring', 4: 'Spring', 5: 'Spring',
                        6: 'Summer', 7: 'Summer', 8: 'Summer',
                        9: 'Autumn', 10: 'Autumn', 11: 'Autumn'}
    months_list_info = ['Winter', 'Winter',
                        'Spring', 'Spring', 'Spring',
                        'Summer', 'Summer', 'Summer',
                        'Autumn', 'Autumn', 'Autumn',
                        'Winter']
    month_number = int(input('Enter month number: '))
    print(f'Dict: {months_dict_info[month_number]}, List: {months_list_info[month_number - 1]}')


@func_name
def task_4():
    user_string = input('Enter string: ')
    words = [string[:10] for string in user_string.split(' ')]
    print(*words, sep='\n')


@func_name
def task_5():
    rating = [7, 5, 3, 3, 2]
    print(f'Rating: {rating}')
    while True:
        new_element = int(input('Enter new element (0 to exit): '))
        if not new_element:
            break
        for index in range(len(rating)):
            if rating[index] < new_element:
                rating.insert(index, new_element)
                break
        else:
            rating.append(new_element)
        print(f'Rating: {rating}')


@func_name
def task_6():
    products = []
    number_of_products = int(input('Enter the number of products: '))
    for product_number in range(number_of_products):
        print(f'> Enter product {product_number + 1}:')
        product_name = input('Product name: ')
        product_price = float(input('Product price: '))
        product_count = int(input('Product count: '))
        product_unit = input('Product unit: ')
        products.append((product_number, {'name': product_name,
                                          'price': product_price,
                                          'count': product_count,
                                          'unit': product_unit}))
    print(products)
    analytics = {}
    for number, features in products:
        for name, value in features.items():
            list_value = analytics.get(name)
            if list_value:
                list_value.append(value)
            else:
                analytics[name] = [value]
    print(analytics)


task_1()
task_2()
task_3()
task_4()
task_5()
task_6()
