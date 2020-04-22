"""
А вот задача посложнее. Напишите на псевдокоде алгоритм игры, в которой случайное число от 1 до 100 загадывает
человек, а отгадывает компьютер. Прежде чем приступать к решению, задумайтесь над тем, какой
должна быть оптимальная стратегия отгадывания. Если алгоритм на псевдокоде будет удачным, попробуйте
реализовать игру на Pythoп.

---------------------------------------------------------------------------

Человек загадывает число и дает команду компьютеру разрешающую отгадывать "поехали".
компьютер выдает число от 1 до 100.
    я говорю "больше"
    или "меньше"
    или "отгадал"
        поздравляет себя с победой
        break
    компьютер выдает число из оставшегося диапозона
    я говорю "больше"
    или "меньше"
    или "отгадал"
        поздравляет себя с победой
        break

"""
import random
min = 1
max = 100
pc_response = random.randint(min, max)
print(pc_response)
answer = input("Правельно?\n")
tries = 1
while True:
    if answer == "больше":
        min = pc_response
    elif answer == "меньше":
        max = pc_response
    elif answer == "правильно":
        print("Ура! Я выиграл!")
        print("Количество попыток:", tries)
        break
    pc_response = random.randint(min + 1, max - 1)
    tries += 1
    print(pc_response)
    answer = input("Правельно?\n")
