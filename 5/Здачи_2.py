# Напишите программу «Генератор персонажей» для ролевой игры. Пользователю должно быть предоставлено
# 30 пунктов, которые можно распределить между четырьмя характеристиками: Сипа, Здоровье, Мудрость
# и Ловкость. Надо сделать так, чтобы пользователь мог не только брать эти пункты из общего «Пупа», но и возвращать
# их туда из характеристик, которым он решит присвоить другие значения.

paragraph = 0
strength = 0
health = 0
wisdom = 0
dexterity = 0
characteristics = ["Сипа", "Здоровье", "Мудрость", "Ловкость"]
points_for_characteristic = 30
point_enter = 0
print("Перед началом игры вам необходимо распределить очки характеристик персонажа:", points_for_characteristic,
      "points\n\n")
while paragraph != 0 or points_for_characteristic != 0:
    print("Ваши характеристики сейчас выглядят так:"
          "\n1 -", characteristics[0], "=", strength,
          "\n2 -", characteristics[1], "=", health,
          "\n3 -", characteristics[2], "=", wisdom,
          "\n4 -", characteristics[3], "=", dexterity,
          "\n0 - Сохранить настройки и Выйти.\n")

    print("У вас для распредиления есть:", points_for_characteristic, "пойнтов.\n")
    paragraph = int(input("Для выбора пункта меню введите его номер: "))
    if paragraph == 1:
        print("Сейчас у вас:", characteristics[0], "=", strength, "\n")
        point_enter = input("Введите количество пунктов которое вы хотите прибавить,\n"
                            "если хотите убавить, введите \"-\" перед числом: ")
        if point_enter == "" or point_enter >= "a" or point_enter <= "#":
            point_enter = "0"
            print("Значение не верно, и приравненно к \"0\"")
        point_enter = int(point_enter)
        if point_enter >= points_for_characteristic:
            print("Веденное количество пунктов больше чем их остаток.\n"
                  "К характеристике добавленно максимальное количество пунктов.")
            point_enter = points_for_characteristic
        elif point_enter < 0 and strength < abs(point_enter):
            print("Веденное количество пунктов больше чем их остаток.\n"
                  "Характеристика уменьшена на максимальное количество пунктов.")
            point_enter = -strength
        if -30 <= point_enter <= 30:
            strength += point_enter
            points_for_characteristic -= point_enter
        else:
            print("Да ты хакер! Или тестишь тихонько?")
    elif paragraph == 2:
        print("Сейчас у вас:", characteristics[1], "=", health, "\n")
        point_enter = input("Введите количество пунктов которое вы хотите прибавить,\n"
                            "если хотите убавить, введите \"-\" перед числом: ")
        if point_enter == "" or point_enter >= "a" or point_enter <= "#":
            point_enter = '0'
        point_enter = int(point_enter)
        if point_enter >= points_for_characteristic:
            print("Веденное количество пунктов больше чем их остаток.\n"
                  "К характеристике добавленно максимальное количество пунктов.")
            point_enter = points_for_characteristic
        elif point_enter < 0 and health < abs(point_enter):
            print("Веденное количество пунктов больше чем их остаток.\n"
                  "Характеристика уменьшена на максимальное количество пунктов.")
            point_enter = -health
        if -30 <= point_enter <= 30:
            health += point_enter
            points_for_characteristic -= point_enter
        else:
            print("Да ты хакер! Или тестишь тихонько?")
    elif paragraph == 3:
        print("Сейчас у вас:", characteristics[1], "=", wisdom, "\n")
        point_enter = input("Введите количество пунктов которое вы хотите прибавить,\n"
                            "если хотите убавить, введите \"-\" перед числом: ")
        if point_enter == "" or point_enter >= "a" or point_enter <= "#":
            point_enter = '0'
        point_enter = int(point_enter)
        if point_enter >= points_for_characteristic:
            print("Веденное количество пунктов больше чем их остаток.\n"
                  "К характеристике добавленно максимальное количество пунктов.")
            point_enter = points_for_characteristic
        elif point_enter < 0 and wisdom < abs(point_enter):
            print("Веденное количество пунктов больше чем их остаток.\n"
                  "Характеристика уменьшена на максимальное количество пунктов.")
            point_enter = -wisdom
        if -30 <= point_enter <= 30:
            wisdom += point_enter
            points_for_characteristic -= point_enter
        else:
            print("Да ты хакер! Или тестишь тихонько?")
    elif paragraph == 4:
        print("Сейчас у вас:", characteristics[1], "=", dexterity, "\n")
        point_enter = input("Введите количество пунктов которое вы хотите прибавить,\n"
                            "если хотите убавить, введите \"-\" перед числом: ")
        if point_enter == "" or point_enter >= "a" or point_enter <= "#":
            point_enter = '0'
        point_enter = int(point_enter)
        if point_enter >= points_for_characteristic:
            print("Веденное количество пунктов больше чем их остаток.\n"
                  "К характеристике добавленно максимальное количество пунктов.")
            point_enter = points_for_characteristic
        elif point_enter < 0 and dexterity < abs(point_enter):
            print("Веденное количество пунктов больше чем их остаток.\n"
                  "Характеристика уменьшена на максимальное количество пунктов.")
            point_enter = -dexterity
        if -30 <= point_enter <= 30:
            dexterity += point_enter
            points_for_characteristic -= point_enter
        else:
            print("Да ты хакер! Или тестишь тихонько?")
    elif paragraph == 0:
        if points_for_characteristic == 0:
            print("Изменения сохранены.")
        else:
            print("У вас еще остались не распределенные характеристики.")
    else:
        print("Такого пункта меню нет.")
input("Нажмите Enter, чтобы выйти.")
