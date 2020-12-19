def task_6_a(start, end):
    from itertools import count

    for value in count(start):
        if value >= end:
            return
        print(value)


def task_6_b(iterable, count):
    from itertools import cycle

    count = abs(count)
    if not count:
        return
    for index, value in enumerate(cycle(iterable), 1):
        print(value)
        if index >= count:
            return


task_6_a(5, 50)
task_6_b([2, 4, 6], 10)
