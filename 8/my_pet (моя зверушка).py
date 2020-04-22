# Моя зверушка
# Виртуальный питомец, о котором пользователь может заботиться.
from random import randint
from math import fabs


class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name, hunger=0, boredom=0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __str__(self):
        return f"Имя зверя: {self.name}. Голог зверя: {self.hunger}. Наигроннасть зверя: {self.boredom}"

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 10:
            m = "прекрасно"
        elif 10 <= unhappiness <= 20:
            m = "неплохо"
        elif 20 <= unhappiness <= 30:
            m = "не сказать чтобы хорошо"
        else:
            m = "ужасно"
        return m

    def talk(self):
        print(f"Меня зовут {self.name} и сейчас я чувствую себя {self.mood}")
        self.__pass_time()

    def eat(self, food=4):
        print("Мрр... Спасибо!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self, fun=1):
        print("Уииии!")
        self.boredom -= fun * 4
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()


def main():
    print("Сколько зверушек вы себе хотите?")
    n = None
    while type(n) != int:
        try:
            n = int(fabs(int(input("Ваш ответ: "))))
        except ValueError:
            print("Попробуйте еще раз.")
    farm = {}
    for i in range(n):
        farm[f"crit_name_{i}"] = input("Как вы назовете свою зверушку?\n\nИмя: ")
    object_farm = []
    p = 0
    for i in farm.keys():
        globals()[i] = Critter(farm.get(i), randint(0, 20), randint(0, 20))
        object_farm.append(i)
        p += 1
    choice = None
    while choice != "0":
        print("""
        Моя зверушка
        0 - Выйти
        1 - Узнать о самочувствии зверушки
        2 - Покормить зверушку
        3 - Поиграть со зверушкой
        """)
        choice = input("Ваш выбор: ")
        print()
        # выход
        if choice == "0":
            print("До свидания.")
        # беседа со зверушкой
        elif choice == "77":
            for i in farm.keys():
                print(globals()[i])
        elif choice == "1":
            for i in farm.keys():
                (globals()[i]).talk()
        # кормление зверушки
        elif choice == "2":
            try:
                kilogram_of_food = int(input("По сколько мяса скормить вашим обжоркам?\nВведите цифрой: КГ= "))
            except ValueError:
                print("Цифру мы не распознали. Поэтому мы решили дать по 5 кг мяса каждой.")
                kilogram_of_food = 5
            if kilogram_of_food > 20:
                kilogram_of_food = 20
            for i in farm.keys():
                (globals()[i]).eat(kilogram_of_food)
        # игра со зверушкой
        elif choice == "3":
            try:
                number_of_games = int(input(f"Сколько дней вы готовы потратить на игру с вашими зверюшками?"
                                            f"\nВведите цифрой: Дней: "))
            except ValueError:
                print("Мы не распознали цыфру, по этому зверушки взмедетнули денечек...")
                number_of_games = 1
            if number_of_games > 5:
                number_of_games = 5
            for i in farm.keys():
                (globals()[i]).play(number_of_games)
        # не понятный пользовательский ввод
        else:
            print(f"Извините, в меню нет пункта {choice}.")


main()
input("\n\nНажмите Enter, чтобы выйти.")
