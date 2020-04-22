# Зверушка с атрибутом
# Демонстрирует работу с атрибутами в методах


class Critter(object):
    """Виртуальный питомец"""

    def __init__(self, name):
        print("Появилась на свет новая зверушка!")
        self.name = name

    def __str__(self):
        rep = "Объект класса Critter\n"
        rep += f"Имя: {self.name}\n"
        return rep

    def talk(self):
        print(f"Привет. Меня завут {self.name}.")

# Основная часть


crit_1 = Critter("Бобик")
crit_1.talk()
crit_2 = Critter("Мурзик")
crit_2.talk()
print("\nВывод объекта crit_1 на экран:")
print(crit_1)
print("Непосредственный доступ к атрибуту crit_1.name:")
print(crit_1.name)
input("\n\nНажмите Enter, чтобы выйти.")