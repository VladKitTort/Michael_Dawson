# Зверушка с конструктором
# Демонстрирует работу конструктора


class Critter(object):
    """Виртуальный питомец"""

    def __init__(self):
        print("Появилась на свет новая зверушка!")

    def talk(self):
        print("Привет. Я зверушка - экземпляр класса Critter.")

# Основная часть


crit_1 = Critter()
crit_2 = Critter()
crit_1.talk()
crit_2.talk()
input("\n\nНажмите Enter, чтобы выйти.")
