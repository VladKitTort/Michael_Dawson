# Доработайте программу «Кто твой папа?» так, чтобы можно было, введя имя человека, узнать, кто его дед.
# Программа должна по-прежнему пользоваться одним словарем с парами «сын - отец».
# Подумайте, как включить в этот словарь несколько поколений.

children_and_fathers = {"Лея": ["Брэдли Купер", "kkk"], "Марк": ["Дмитрий Маликов", "LLL"],
                        "Луна": ["Джон Ледженд", "OOO"],
                        "Майлз": ["Джон Ледженд", "IIII"], "Луи Уилья": ["Принц Уильям", "UUU"],
                        "Эвелин": ["Брюс Уиллис", "PPPP"],
                        "Рэй": ["Брюс Уиллис", "RRRR"], "Уильяму": ["Джимми Киммел", "TTTT"]}
choice = ""
while choice != "0":
    print(
        """
        Дети и их отцы.
        0 - Выйти.
        1 - Показать все данные базы ребенок - отец - дед.
        2 - Показать Имя деда по имяни ребенка.
        3 - Показать Имя отца по имяни ребенка.
        4 - Добавить пару ребенок - отец.
        5 - Заменить пару ребенок - отец.
        6 - Удалить пару ребенок - отец.
        """
    )
    choice = input("Выбирите пункт меню: ")
    if choice == "0":
        print("До свидания.")
    elif choice == "1":
        print("\nСуществующие данные базы\n")
        print("Ребенок - Отец - Дед")
        for two in children_and_fathers:
            print(two, "-", children_and_fathers[two][0], "-", children_and_fathers[two][1])
    elif choice == "2":
        son_name = input("Введите имя ребенка: ")
        if son_name not in children_and_fathers:
            print("Деда с таким внуком в базе нет.")
        else:
            print("Дед внука с имянем ", son_name, " это ", children_and_fathers[son_name][1], "!", sep="")
    elif choice == "3":
        son_name = input("Введите имя ребенка: ")
        if son_name not in children_and_fathers:
            print("Отца с таким ребенком в базе нет.")
        else:
            print("Отец ребенка с имянем ", son_name, " это ", children_and_fathers[son_name][0], "!", sep="")
    elif choice == "4":
        son_name = input("Введите имя ребенка: ")
        father_name = input("Введите имя отца: ")
        grandpa_name = input("Введите имя деда: ")
        if son_name not in children_and_fathers:
            children_and_fathers[son_name] = [father_name, grandpa_name]
            print("Новая запись добавлена.")
        else:
            print("Такая запись в базе уже существует.")
    elif choice == "5":
        son_name = input("Введите имя ребенка: ")
        father_name = input("Введите имя отца: ")
        grandpa_name = input("Введите имя деда: ")
        father_name_new = input("Введите новое имя отца: ")
        grandpa_name_new = input("Введите новое имя деда: ")
        if son_name not in children_and_fathers:
            print("Такой записи в базе нет.")
        else:
            children_and_fathers.update({son_name: [father_name_new, grandpa_name_new]})
            print("Замена произведена.")
    elif choice == "6":
        son_name = input("Введите имя ребенка: ")
        father_name = input("Введите имя отца: ")
        grandpa_name = input("Введите имя деда: ")
        if son_name not in children_and_fathers:
            print("Такой записи в базе нет.")
        else:
            del children_and_fathers[son_name]
            print("Такой записи в базе больше нет.")
    else:
        print("Такого пункта в меню нет.")
input("Нажмите Enter, чтобы выйти.")
