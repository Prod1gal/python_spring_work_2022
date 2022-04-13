#Единицы массы пронумерованы следующим образом: 1 — килограмм, 2 — миллиграмм, 3 — грамм, 4 — тонна, 5 — центнер.
#Дан номер единицы массы и масса тела M в этих единицах (вещественное число). Вывести массу данного тела в килограммах.
# Данную задачу нужно решить с помощью конструкции  match  (Python v3.10)


# Пример:
# Введите единицу массы тела
#       1 - килограмм
#       2 — миллиграмм
#       3 — грамм
#       4 — тонна
#       5 — центнер
# >4
#
# #Введите  массу тела
# >1
#
# Ответ: 1000 кг


# первое решение без match

# print("Единицы массы пронумерованы следующим образом:")
# print("1 - килограмм")
# print("2 — миллиграмм")
# print("3 — грамм")
# print("4 — тонна")
# print("5 — центнер")
#
# mass_unit = int(input("Введите единицу массы тела:"))
# while mass_unit > 5 or mass_unit < 0:
#     mass_unit = int(input("Нужно выбрать единицу измерения от 1 до 5, введите число снова:"))
# if mass_unit == 1:
#     weight_body = int(input("Введите массу тела в килограммах:"))
#     print("Масса тела:", weight_body, "кг")
# elif mass_unit == 2:
#     weight_body = int(input("Введите массу тела в миллиграммах:"))
#     weight_body = weight_body / 10 ** 6
#     print("Масса тела:", weight_body, "кг")
# elif mass_unit == 3:
#     weight_body = int(input("Введите массу тела в граммах:"))
#     weight_body = weight_body / 1000
#     print("Масса тела:", weight_body, "кг")
# elif mass_unit == 4:
#     weight_body = int(input("Введите массу тела в тоннах:"))
#     weight_body = weight_body * 1000
#     print("Масса тела:", weight_body, "кг")
# elif mass_unit == 5:
#     weight_body = int(input("Введите массу тела в центнерах:"))
#     weight_body = weight_body * 100
#     print("Масса тела:", weight_body, "кг")



# второе решение с match

print("Единицы массы пронумерованы следующим образом:")
print("1 - килограмм")
print("2 — миллиграмм")
print("3 — грамм")
print("4 — тонна")
print("5 — центнер")

mass_unit = int()

def check_weight(mass_unit):
    mass_unit = int(input("Введите единицу массы тела:"))
    match mass_unit:
        case 1:
            weight_body = int(input("Введите массу тела в килограммах:"))
            print("Масса тела:", weight_body, "кг")
        case 2:
            weight_body = int(input("Введите массу тела в миллиграммах:"))
            weight_body = weight_body / 10 ** 6
            print("Масса тела:", weight_body, "кг")
        case 3:
            weight_body = int(input("Введите массу тела в граммах:"))
            weight_body = weight_body / 1000
            print("Масса тела:", weight_body, "кг")
        case 4:
            weight_body = int(input("Введите массу тела в тоннах:"))
            weight_body = weight_body * 1000
            print("Масса тела:", weight_body, "кг")
        case 5:
            weight_body = int(input("Введите массу тела в центнерах:"))
            weight_body = weight_body * 100
            print("Масса тела:", weight_body, "кг")
        case _:
            raise ValueError("Неверный тип данных. Перезапустите программу.") #почему-то ругается на int в первой переменной и не выполняется

    return(print("Зашибись!"))

check_weight(mass_unit)