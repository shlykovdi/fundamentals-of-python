# I used functions because I don't want variable names to overlap.


def func_name(func):
    def decorator(*args, **kwargs):
        print(f'>> {func.__name__.capitalize().replace("_", "-")}:')
        func(*args, **kwargs)
        print('')
    return decorator


@func_name
def task_1():
    x = int(input('Input number X: '))
    y = int(input('Input number Y: '))
    str_a = str(input('Input string A: '))
    str_b = str(input('Input string B: '))
    print(f'User input numbers {x} and {y} and two strings "{str_a}" and "{str_b}"')


@func_name
def task_2():
    seconds = int(input('Input time in seconds: '))
    hh = (seconds // 60 // 60) % 24
    mm = (seconds // 60) % 60
    ss = seconds % 60
    print('Time: {0:0>2d}:{1:0>2d}:{2:0>2d}'.format(hh, mm, ss))


@func_name
def task_3():
    n = int(input('Input number N to calculate (n + nn + nnn): '))
    nn = int(str(n) * 2)
    nnn = int(str(n) * 3)
    print(f'Sum: {n + nn + nnn}')


@func_name
def task_4():
    x = int(input('Input number: '))
    max_digit = 0
    while x > 0:
        digit = x % 10
        if digit > max_digit:
            max_digit = digit
        x //= 10
    print(f'Max digit: {max_digit}')


@func_name
def task_5():
    proceeds = float(input('Enter Proceeds: '))
    costs = float(input('Enter Costs: '))
    profit = proceeds - costs
    if profit > 0.0:
        print('The firm made a profit')
        print('Profitability of proceeds: {0:<.2f}'.format(profit / proceeds))
        number_employes = int(input('Enter number of employes: '))
        print('Profit of each employee: {0:<.2f}'.format(profit / number_employes))
    else:
        print('The firm made a loss')


@func_name
def task_6():
    a = float(input('Input A: '))
    b = float(input('Input B: '))
    days = 1
    print('Day {0}: {1:<.2f} km'.format(days, a))
    while a < b:
        a *= 1.1
        days += 1
        print('Day {0}: {1:<.2f} km'.format(days, a))
    print(f'Answer: on the {days}th day, the athlete achieved a result of at least {b} km.')


task_1()
task_2()
task_3()
task_4()
task_5()
task_6()
