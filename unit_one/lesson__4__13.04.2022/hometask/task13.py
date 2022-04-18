#todo: Дан целочисленный массив размера N из 10 элементов.
#Преобразовать массив, увеличить каждый его элемент на единицу.


from array import *

print("Сначала дан вот такой массив:")
first_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(first_array)
n = len(first_array)

for i in range(n):
    first_array[i] += 1
print("Теперь к каждому элементу прибавилась 1-ца:")
print(first_array)



