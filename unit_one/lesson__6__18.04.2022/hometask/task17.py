#todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
# Функция должна принимать 1 параметр - словарь, в котором указано количество единиц товара.
# Цены хранятся в словаре:
# prices = {
#   "banana": 4,
#   "apple": 2,
#   "orange": 1.5,
#   "pear": 3
# }


prices = {
  "banana": 4,
  "apple": 2,
  "orange": 1.5,
  "pear": 3
}

def compute_bill(bill):
    result = 0
    for key, value in bill.items():
        print("-", key, ":", value)
        result = result + value
    return result

print("Итоговая сумма товаров в чеке:", compute_bill(prices))