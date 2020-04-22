# Доработайте новую версию игры «Опадай число» (которую вы создали, решая предыдущую задачу) так, чтобы
# основная часть программы стала функцией main(). Для того чтобы игра началась, не забудьте вызвать эту
# функцию глобально.

import random


def instruction():
    print("""
    \tДобро пожаловать в игру \"Отгадай число!\"
    \nЯ загадал натуральное число из диапозона от 1 до 100.
    Посторайтесь отгадать его за 4 попытки.\n
    """)


def ask_number(question, low=1, high=101, multiplicity=1):
    """Просит ввести число из диапозона."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response * multiplicity


def hidden_number(low=1, high=101):
    the_number = random.randint(low, high)
    return the_number


def main():
    the_number = hidden_number()
    tries = 0
    attempts = 3
    instruction()
    guess = ask_number("Ваше предположение: ")
    while True:
        if guess == the_number:
            print("Вы выиграли!")
            print("Загаданным числом было:", the_number)
            print("Вы затратили на отгадывание числа, всего лишь", tries, " попыток!\n")
            break
        if guess > the_number:
            print("Меньше..")
        else:
            print("Больше...")
        if tries > attempts:
            print("Вы проиграли")
            print("Загаданным числом было:", the_number)
            break
        guess = ask_number("Ваше предположение: ")
        tries += 1


main()
input("\n\nНажмите Enter, чтобы выйти.")
