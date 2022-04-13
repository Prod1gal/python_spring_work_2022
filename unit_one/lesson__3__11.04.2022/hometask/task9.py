# todo:  Даны три переменные: X, Y, Z. Их значения числа.
# Из данных произвольных чисел выбрать наибольшее.

# Пример:
# X = 5
# Y = 10
# Z = 3
# Ответ: Наибольшее число 10.
#
# X = 10
# Y = 12
# Z = -7
# Ответ: Наибольшее число 12.


import random

x = random.randint(-100, 100)
y = random.randint(-100, 100)
z = random.randint(-100, 100)
print(x, "- это число х")
print(y, "- это число y")
print(z, "- это число z")

largest_number = 0

if x > y and x > z:
    largest_number = x
if y > x and y > z:
    largest_number = y
if z > y and z > x:
    largest_number = z

print(largest_number, "- это наибольшее число")