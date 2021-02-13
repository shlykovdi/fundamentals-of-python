import sys

from task_5 import (Company, run)
from task_3 import (IsNotNumberError, input_number)


try:
    count = input_number('Enter number of equipments: ')
except IsNotNumberError as error:
    print(error)
    sys.exit(-1)

run(Company, lambda: count)
