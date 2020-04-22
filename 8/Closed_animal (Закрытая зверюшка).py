# Закрытая зверушка
# Демонстрирует закрытые переменные и методы


class Critter(object):
    """Виртуальный питомец"""

    total = 0

    @staticmethod
    def status():
        print(f"\nВсего зверушек сейчас: {Critter.total}")

    def __init__(self, name, mode):
        print("Появилась на свет новая зверушка!")
        self.name = name  # открытый атрибут
        self.__mode = mode  # закрытый атрибут
        Critter.total += 1

    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += f"Имя: {self.name}\n"
        return rep

    def talk(self):
        print(f"Привет. Меня завут {self.name}.")
        print(f"Сейчас я чувсствую себя {self.__mode}.\n")

    def __private_method(self):
        print("Это закрытый метод.")

    def public_method(self):
        print("Это открытый метод")
        self.__private_method()

# Основная часть


crit = Critter("Бобик", "прерасно")
crit.talk()
crit.public_method()

input("\n\nНажмите Enter, чтобы выйти.")