#todo: Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.

# Пример:
#           1             6      9
# mass = [1,2,17,16,30,51,2,70,3,2]
#
# Для числа 2 индексы двух ближайших чисел: 6 и 9
#
# Пример:
#           1             6     9
# mass = [1,2,17,54,30,89,2,1,6,2]
# Для числа 1 индексы двух ближайших чисел: 0 и 7
# Для числа 2 индексы двух ближайших чисел: 6 и 9

# определить индексы повторяющихся чисел, а затем вывести номера тех индексов, которые ближе друг к другу


from random import randint

first_array = [randint(1, 10) for i in range(10)]
print("Сначала дан вот такой массив:")
print(first_array)

result_index = []
count_index = 0

value = int(input("Введите число из массива для поиска двух ближайших индексов: "))

for i in first_array:
    index_count = count_index + 1
    if value == i:
        result_index.append(count_index-1)

if (first_array.count(value) >= 2) and (first_array.count(value) <= 4):
    print("Число представлено в массиве", first_array.count(value), "раза")
else:
    print("Число представлено в массиве", first_array.count(value), "раз")

if (first_array.count(value) == 1) or (first_array.count(value) == 0):
    print("Так как искомое число в массиве представлено один раз, у него не будет двух ближайших индексов")
else:
    if len(result_index) > 2:
        print("Для числа", value, "индексы двух ближайших чисел", result_index[1],"и",result_index[2])
    else:
        print("Для числа", value, "индексы двух ближайших чисел", result_index[0],"и",result_index[1])




#
# first_array.sort()
#
# for i in range(0,len(first_array)-1):
#     if first_array[i] == first_array[i+1]:
#         # не получается обработать дублирование
#         print(str(first_array[i]) + '- это число дублируется')
#
# # def org_app(first_array, refArray):
# #     out1 = np.empty(first_array.size, dtype=int)
# #     for i, value in enumerate(first_array):
# #         # find_nearest from posted question
# #         index = find_nearest(refArray, value)
# #         out1[i] = index
# #     return out1
#
#
# i = int(input("Введите значение элемента, чтобы найти его ближайшие индексы:"))
#
# def find_closest(first_array, i):
#     idx = first_array.searchsorted(i)
#     idx = np.clip(idx, 1, len(first_array)-1)
#     left = first_array[idx-1]
#     right = first_array[idx]
#     idx -= i - left < right - i
#     return print(idx)
# find_closest(first_array, i)



