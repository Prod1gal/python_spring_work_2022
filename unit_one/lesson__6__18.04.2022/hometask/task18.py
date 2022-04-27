
#todo:Создайте программу, которая будет выводить все возможные комбинации при броске 2 игральных костей
# и сумму их значений. У игральной кости стороны пронумерованы от 1 до 6.
#
# Пример вывода:
# Сумма 2   комбинация [(1,1)]
# Сумма 3   комбинация [(1,2),(2,1)]
# Сумма 4   комбинация [(1,3),(3,1),(2,2)]
# ........................................
# Выводы комбинаций оформить в список кортежей.


import random


def count_bones(combination):
    s_list = []
    summa = combination[0] + combination[1]
    for a in range(1, 7):
        for b in range(1, 7):
            if (a + b == summa):
                s_list.append((a, b,))
    tuple_list = sorted(tuple(s_list))
    return tuple_list


def show_result(result, options):
    summa_print = sum(result)
    print("Сумма", summa_print, "  ", "комбинация", options)
    print("." * 45)


def random_bones():
    first_bone = random.randrange(1, 6)
    second_bone = random.randrange(1, 6)
    return first_bone, second_bone


combination = random_bones()
count = count_bones(combination)
show_result(combination, count)
