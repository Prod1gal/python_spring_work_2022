#todo: Для написанной игры "Поле чудес" нужно сделать рефакторинг кода , сгруппировать
# функционал в логические блоки и оформить эти блоки кода в виде функций. Стараться
# чтобы каждая функция выполняла одно универсальное действие.


import random

number_try = 5
words = ["энциклопедия", "циферблат", "брови", "тюрьма", "апач", "утираться"]
riddle_ = ["Однажды в знаменитую французскую тюрьму Бастилию заключили не человека, а некое издание. Какое? (12 букв)",
         "Шведский учёный Карл Линней однажды заметил интересное свойство цветов. Благодаря этой их особенности в 1720 году"
         "\nв городе Уппсала он создал первый в мире цветочный… Что? (9 букв)",
         "Древние египтяне считали кошку священным животным. Когда питомец умирал, для людей это было большим горем."
         "\nВ знак траура они избавлялись от… Чего? Ответ дайте во множественном числе. (5 букв)",
         "В ЮАР есть одна редкая достопримечательность — бар внутри огромного баобаба, куда могут одновременно поместиться 15 человек."
         "\nА в качестве чего использовали баобабы в XIX веке в Австралии? (6 букв)",
         "В своих номерах клоуны часто исполняют ложную пощёчину. В момент, когда один артист бьёт другого по лицу, тот незаметно хлопает в ладоши. "
         "\nКаким цирковым термином обозначается такая пощёчина? (4 буквы)",
         "Солдат при Петре I набирали в основном из крестьян. Чтобы сохранить подольше сукно, из которого для них шились мундиры, "
         "\nцарь издал указ: пришивать на лицевую сторону рукавов пуговицы, чтобы солдаты не могли… Делать что? (9 букв)"]

word_random = str(random.choice(words))
word_random_list = [word_random]

print(riddle_[words.index(word_random)])
word_mask = "▒" * len(word_random)
print('Отгадываемое слово: ', ' '.join(word_mask))
word_list = list(word_mask)
word_order = [ord(x) for x in word_random]

buffer = []
order_letter = buffer

def entrance():
    first_enter = str(input("Назовите букву: "))
    return first_enter


def in_buffer(find_letter):
    letter = find_letter
    if letter in word_random:
        return buffer.append(order_letter)


def try_to_find(letter, count_letter, b, count_list, order_letter):
    global number_try
    if count_letter >= 1:
        print("Откройте букву!")
        for i in word_random:
            if i == letter:
                count_list.append(word_random.index(letter, b))
                b = count_list[-1] + 1
        if letter in word_random:
            for f in count_list:
                word_list[f] = word_random[f]
                if "".join(word_list) == word_random:
                    print("*" * 45, "\nИииии перед нами победитель капитал-шоу Поле чудес!!!")
                    number_try = 0
                    print("*" * 45)
        print(" ".join(word_list))
    else:
        number_try -= 1
        print("*" * 45)
    return number_try


def main(main_letter, number_try):
    if len(main_letter) > 1:
        print("Нужно назвать только одну букву, не пытайтесь обмануть Якубовича!")
        number_try -= 1
        if (number_try <= 4) or (number_try >= 2):
            print("Нет такой буквы!\nЕсть ещё", number_try, "попытки.")
        elif number_try == 1:
            print("Нет такой буквы!\nЕсть ещё", number_try, "попытка.")
        else:
            print("Нет такой буквы! Вы не угадали! Отгадываемым словом было", word_random)

    else:
        order_letter = ord(main_letter)
        if order_letter in buffer:
            print("Эта буква уже есть в слове, используйте другую.")
            print(" ".join(word_list))
        else:
            in_buffer(main_letter)

    return main_letter


def end_games(): return print("\nПодарки первой тройке игроков....в студию!")


while number_try > 0:
    clist = []
    arg_b = 0
    arg_letter = entrance()
    if arg_letter == 'quit' or arg_letter == 'выход':
        break
    main_game = main(arg_letter, number_try)
    arg_count_letter = word_random.count(main_game)
    order_letter = buffer
    arg_a = number_try
    end_game = try_to_find(main_game, arg_count_letter, arg_b, clist, order_letter)
else:
    end_games()