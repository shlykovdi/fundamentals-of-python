def func_name(func):
    def decorator(*args, **kwargs):
        print(f'>> {func.__name__.capitalize().replace("_", "-")}:')
        func(*args, **kwargs)
        print('')

    return decorator


@func_name
def task_1():
    def sum_numbers(x, y):
        if y == 0:
            raise ZeroDivisionError
        return x / y

    try:
        number_x = float(input('Enter number X: '))
        number_y = float(input('Enter number Y: '))
    except ValueError as error:
        print(f'Wrong input numbers ({error}).')
        return

    try:
        result = sum_numbers(number_x, number_y)
    except ZeroDivisionError as error:
        print(f'Zero division ({error})')
        return

    print(result)


@func_name
def task_2():
    def user_info(first_name: str = '', second_name: str = '', born_year: int = 0, city: str = '', email: str = '', phone_number: str = ''):
        print(locals())  # Вывдел одной строкой, как требовалось в задании

    user_info(first_name='Vasya', second_name='Pupkin', born_year=1954, city='Moscov', email='vasya.pupkin@gmail.com', phone_number='8800300600')


@func_name
def task_3():
    def my_func(a, b, c):
        return sum(sorted(locals().values(), reverse=True)[:2])

    print(my_func(20, 4, 50))


@func_name
def task_4():
    class WrongTypesPowException(Exception):
        pass

    def my_func(x, y, use_cycle=False):
        if not isinstance(x, float) or not isinstance(y, int):
            raise WrongTypesPowException

        if use_cycle:
            result = 1.0
            for _ in range(abs(y)):
                result *= x
            return 1.0 / result if y < 0 else result
        else:
            return x ** y

    try:
        result1 = my_func(3.14, -5)
        result2 = my_func(3.14, -5, use_cycle=True)
    except WrongTypesPowException:
        print('WrongTypesPowException')
        return

    print(result1, result2, sep='\n')


@func_name
def task_5():
    common_sum = 0
    while True:
        input_numbers = input('Enter numbers (~ to exit): ').split()
        if '~' in input_numbers:
            try:
                common_sum += sum(map(int, input_numbers[:input_numbers.index('~')]))
            except ValueError as error:
                print(f'Wrong input number ({error})')
                continue

            print(f'Common sum = {common_sum}')
            break
        else:
            try:
                common_sum += sum(map(int, input_numbers))
            except ValueError as error:
                print(f'Wrong input number ({error})')
                continue

        print(f'Common sum = {common_sum}')


@func_name
def task_6():
    def int_func(word):
        return word.capitalize()

    string = input('Enter string: ')
    string = ' '.join(map(int_func, string.split()))
    print(string)


def task_exec():
    tasks = (task_1, task_2, task_3, task_4, task_5, task_6)
    while True:
        try:
            task_number = int(input('>> Enter task number to Run (0 to exit): '))
        except ValueError as error:
            print(f'Wrong input number ({error})')
            continue

        if not task_number:
            break

        if task_number in range(1, len(tasks) + 1):
            tasks[task_number - 1]()
        else:
            print('Task not found')


task_exec()
