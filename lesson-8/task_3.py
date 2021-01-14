from typing import Union


class IsNotNumberError(Exception):
    pass


def input_number(text: str = None) -> Union[int, float, None]:
    text = input(text if text else 'Enter number ("stop" to exit): ')

    if text == 'stop':
        return None

    try:
        result = int(text)
    except ValueError:
        try:
            result = float(text)
        except ValueError:
            raise IsNotNumberError('This text is not a number!')

    return result


def run() -> None:
    number_list = []
    while True:
        try:
            number = input_number()
        except IsNotNumberError as error:
            print(error)
            continue

        if number is None:
            break

        number_list.append(number)

    print(f'Result number list: {number_list}')


if __name__ == '__main__':
    run()
