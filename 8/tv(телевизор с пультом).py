# Задание 2.
# Эмитация телевизора

from random import randint
from math import fabs


class MyTv(object):
    """Эмитация телевизора"""

    def __init__(self, channel="Первый", volume=15):
        self.channel = channel
        self.volume = volume
        self.channels = ["Первый", "Россия", "ТНТ", "НТВ", "СТС", "МУЛЬТ", "Nickelodeon", "2x2", "Фильмы"]

    def remote_control(self):
        #  сохронение канала
        try:
            self.channel = self.channels[MyTv.choice_channel() - 1]
        except IndexError:
            pop = randint(0, 8)  # Рандомный выбор канала
            print(f"Палец попал на случайный канал.")
            self.channel = self.channels[pop]

    @staticmethod
    def choice_channel():
        #  выбор канала
        print("""
        Список канало:
        1 - Первый
        2 - Россия
        3 - ТНТ
        4 - НТВ
        5 - СТС
        6 - МУЛЬТ
        7 - Nickelodeon
        8 - 2x2
        9 - Фильмы
        """)
        try:
            return int(input("Введите цифру канала.\nВаш выбор: "))
        except ValueError:
            pop = randint(0, 8)  # Рандомный выбор канала
            print(f"Палец попал на случайный канал.")
            return pop

    def tv_volume(self):
        print("""
        "-" - убавить громкость
        "+" - добавить громкость
        """)
        try:
            num_volume = input("Ваш выбор: ")
            if num_volume == "-":
                pop = int(input("На сколько убавить звук: "))
                self.volume -= pop
                if self.volume <= 0:
                    print("Звук на минимуме.")
                    self.volume = 0
                elif self.volume >= 50:
                    self.volume += pop
                    print("Звук не изменился.")
            elif num_volume == "+":
                pop = int(input("На сколько увеличить звук: "))
                self.volume += pop
                if self.volume >= 50:
                    print("Звук на максимуме.")
                    self.volume = 50
                elif self.volume <= 0:
                    self.volume -= pop
                    print("Звук не изменился.")
            else:
                print("Звук не изменился.")
        except ValueError:
            print("Звук не изменился.")


def main():
    user_1 = MyTv()
    print("""
            У вас в руках пульт от телевизора, что вы будете делать?
            0 - Вкл
            Ну или положите его на место, и займитесь чем нибудь полезным.
            """)
    inclusion = input("Ваш выбор: ")
    if inclusion == "0":
        selecting_an_operator = None
        while selecting_an_operator != "0":
            print(f"\nВы смотрите канал \"{user_1.channel}\" на громкости \"{user_1.volume}\"")
            print("""
            Ура! телевизор включился. Что будем смотреть?
            0 - Выкл
            1 - Выборать канал
            2 - Изменить громкость
            """)
            selecting_an_operator = input("Ваш выбор: ")
            if selecting_an_operator == "0":
                #  Выключение телевизора
                print("До свидания.")
            elif selecting_an_operator == "1":
                # Вызов выбора каналов
                user_1.remote_control()
            elif selecting_an_operator == "2":
                # изменить гормкость
                user_1.tv_volume()
    else:
        print("До свидания!")


main()
input("\n\nНажмите Enter, чтобы выйти.")
