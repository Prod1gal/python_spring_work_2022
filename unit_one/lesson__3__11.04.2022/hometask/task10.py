# todo: Проверить истинность высказывания: "Данное четырехзначное число читается одинаково
# слева направо и справа налево".


while True:
  try:
    number = str(int(input("Введите любое четырехзначное число:")))
    if len(number) > 4:
      print("Нужно ввести именно четырехзначное число!")
    else:
      break
  except ValueError:
    print("Повторяю - нужно ввести ЧИСЛО!")
if str(number) == str(number)[::-1]:
    print("Число одинаково читается, тогда значение -", bool(number))
else:
    print("Ваше число не читается одинаково, тогда значение -", bool())



