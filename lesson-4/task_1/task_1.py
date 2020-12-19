import sys


def calc_salary(production: int, rate: int, bonus: float) -> float:
    return production * rate + bonus


if __name__ == '__main__':
    if len(sys.argv) < 4:
        print('Wrong arguments count. Need 4 arguments.')
        sys.exit()

    try:
        production_in_hours = int(sys.argv[1])
        rate_in_hours = int(sys.argv[2])
        employee_bonus = float(sys.argv[3])
    except ValueError as error:
        print(error)
        sys.exit()

    print(f'Employee salary = {calc_salary(production_in_hours, rate_in_hours, employee_bonus)}')
