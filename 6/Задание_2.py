# Доработайте игру «Отгадай число» из главы З так, чтобы в ней нашла применение функция ask_number().
import random


def ask_number(question, low=1, high=101, multiplicity=1):
    """Просит ввести число из диапозона."""
    response = None
    while response not in range(low, high):
        response = int(input(question))
    return response * multiplicity


print("\tДобро пожаловать в игру \"Отгадай число!\"")
print("\nЯ загадал натуральное число из диапозона от 1 до 100.")
print("Посторайтесь отгадать его за 4 попытки.\n")
# начальные значения
the_number = random.randint(1, 100)
guess = ask_number("Ваше предположение: ")
tries = 1
# Цикл отгадывания
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
    if tries > 3:
        print("Вы проиграли")
        print("Загаданным числом было:", the_number)
        break
    guess = ask_number("Ваше предположение: ")
    tries += 1
input("\n\nНажмите Enter, чтобы выйти.")