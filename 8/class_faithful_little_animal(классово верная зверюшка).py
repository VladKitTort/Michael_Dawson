# Классовая зверушка
# Демонстрирует работу классов


class Critter(object):
    """Виртуальный питомец"""

    total = 0

    @staticmethod
    def status():
        print(f"\nВсего зверушек сейчас: {Critter.total}")

    def __init__(self, name):
        print("Появилась на свет новая зверушка!")
        self.name = name
        Critter.total += 1

    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += f"Имя: {self.name}\n"
        return rep

    def talk(self):
        print(f"Привет. Меня завут {self.name}.")

# Основная часть


crit_1 = Critter("Бобик")
crit_2 = Critter("Волк")
crit_3 = Critter("Сурок")

Critter.status()
print("\nОбращаюсь к атрибуту класса через объект:", end=" ")
print(crit_1.total)

input("\n\nНажмите Enter, чтобы выйти.")