# todo: Дан номер некоторого года (положительное целое число).
# Вывести соответствующий ему номер столетия, учитывая, что, к примеру, началом 20 столетия был 1901 год.

import random

year_number = random.randint(1901,2022)
print("Выбранный год:", year_number)

if year_number % 100 > 0:
    century_number = year_number // 100 + 1
else:
    century_number = year_number // 100
print("Полученный год:", century_number, "-ое столетие")