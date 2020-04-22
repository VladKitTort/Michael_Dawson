# Просто зверушка
# Демонстрирует простейший класс и объект


class Critter(object):
    """Виртуальный питомец"""
    def talk(self):
        print("Привет. Я зверушка - экземпляр класса Critter.")

# Основная часть


crit = Critter()
crit.talk()
input("\n\nНажмите Enter, чтобы выйти.")
