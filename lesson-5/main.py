def func_name(func):
    def decorator(*args, **kwargs):
        print(f'>> {func.__name__.capitalize().replace("_", "-")}:')
        func(*args, **kwargs)
        print('')

    return decorator


@func_name
def task_1():
    string_lines = []
    while True:
        string = input('Enter string: ')
        if string:
            string_lines.append(string)
        else:
            break

    try:
        with open('task_1.txt', 'w') as file:
            file.writelines(string_lines)
            print(f'The file "{file.name}" was written!')
    except IOError as error:
        print(f'Error write file ({error})')


@func_name
def task_2():
    try:
        with open('task_2.txt', 'r') as file:
            content = file.read()
    except IOError as error:
        print(f'Error read file ({error})')
        return

    import re
    strings = content.split('\n')
    word_count = 0
    pattern = re.compile(r'\w+')
    for string in strings:
        word_count += len(pattern.findall(string))

    print(f'String count = {len(strings)}\nWord count = {word_count}')


@func_name
def task_3():
    try:
        with open('task_3.txt', 'r') as file:
            content = file.read()
    except IOError as error:
        print(f'Error read file ({error})')
        return

    strings = content.split('\n')
    salary_info_list = []
    for string in strings:
        employee_info = tuple(string.split())
        if len(employee_info) < 2:
            continue

        second_name, salary = employee_info
        salary = int(salary)
        salary_info_list.append(salary)
        if salary < 20000:
            print(f'{second_name} has salary: {salary}')

    import functools
    avg_profit = functools.reduce(lambda lhs, rhs: lhs + rhs, salary_info_list) / len(salary_info_list)
    print('Average profit of employees: {0:<.2f}'.format(avg_profit))


@func_name
def task_4():
    try:
        with open('task_4_src.txt', 'r') as file:
            content = file.read()
    except IOError as error:
        print(f'Error read file ({error})')
        return

    string_list = content.split('\n')
    numeral_dict = {1: 'Один', 2: 'Два', 3: 'Три', 4: 'Четыре'}
    new_string_list = []
    for string in string_list:
        if not string:
            continue
        string_items = string.split('-')
        if len(string_items) < 2:
            continue
        numeral_value = numeral_dict.get(int(string_items[1]))
        if numeral_value:
            new_string_list.append(f'{numeral_value} - {string_items[1].strip()}\n')

    try:
        with open('task_4_dst.txt', 'w') as file:
            file.writelines(new_string_list)
            print(f'The file "{file.name}" was written!')
    except IOError as error:
        print(f'Error write file ({error})')


@func_name
def task_5():
    try:
        import random
        with open('task_5.txt', 'w') as file:
            for _ in range(128):
                file.write(f'{str(random.randint(0, 128))} ')
    except IOError as error:
        print(f'Error write file ({error})')
        return

    try:
        with open('task_5.txt', 'r') as file:
            content = file.read()
    except IOError as error:
        print(f'Error read file ({error})')
        return

    import functools
    numbers = content.split()
    print(f'Sum = {functools.reduce(lambda lhs, rhs: lhs + rhs, map(int, numbers))}')


@func_name
def task_6():
    try:
        with open('task_6.txt', 'r') as file:
            content = file.read()
    except IOError as error:
        print(f'Error read file ({error})')
        return

    import re
    pattern = re.compile(r'\d+')
    subject_schedule = content.split('\n')
    subject_occupation_count = {}
    for subject in subject_schedule:
        if not subject:
            continue
        subject_name, *occupations = subject.split()
        common_count = 0
        for occupation in occupations:
            for concrete_occupation in pattern.findall(occupation):
                try:
                    common_count += int(concrete_occupation)
                except ValueError:
                    continue

        subject_occupation_count[subject_name.replace(':', '')] = common_count

    print(subject_occupation_count)


@func_name
def task_7():
    company_profit_info = {}
    company_avg_profit_info = {}
    try:
        with open('task_7.txt', 'r') as file:
            avg_profit = 0.0
            avg_count = 0
            for company in file:
                if not company:
                    continue
                name, type_of_ownership, proceeds, costs = company.split()
                profit = int(proceeds) - int(costs)
                if profit > 0:
                    avg_profit += profit
                    avg_count += 1
                company_profit_info[name] = profit
            company_avg_profit_info['average_profit'] = avg_profit / avg_count if avg_count else 0.0
    except IOError as error:
        print(f'Error read file ({error})')
        return

    company_info_list = [company_profit_info, company_avg_profit_info]

    import json
    try:
        with open('task_7_result.json', 'w') as file:
            json.dump(company_info_list, file)
            print(f'The file "{file.name}" was written!')
    except IOError as error:
        print(f'Error write file ({error})')
        return


def task_exec():
    tasks = (task_1, task_2, task_3, task_4, task_5, task_6, task_7)
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
