# Напишите программу «Кто твой папа?», в которой пользователь будет вводить имя человека,
# а программа- называть отца этого человека. Чтобы было интереснее, можно «научить» программу
# родственным отношениям среди литературных персонажей, исторических лиц и современных знаменитостей.
# Предоставьте пользователю возможность добавлять, заменять и удалять пары «СЫН - отец».

children_and_fathers = {"Лея": "Брэдли Купер", "Марк": "Дмитрий Маликов", "Луна": "Джон Ледженд",
                        "Майлз": "Джон Ледженд", "Луи Уилья": "Принц Уильям", "Эвелин": "Брюс Уиллис",
                        "Рэй": "Брюс Уиллис", "Уильяму": "Джимми Киммел"}
choice = ""
son_name = ""
a = 0
while choice != "0":
    print(
        """
        Дети и их отцы.
        0 - Выйти.
        1 - Показать все пары ребенок - отец.
        2 - Показать Имя отца по имяни ребенка.
        3 - Добавить пару ребенок - отец.
        4 - Заменить пару ребенок - отец.
        5 - Удалить пару ребенок - отец.
        """
    )
    choice = input("Выбирите пункт меню: ")
    if choice == "0":
        print("До свидания.")
    elif choice == "1":
        print("\nСуществующие Пары\n")
        print("Ребенок - Отец")
        for two in children_and_fathers:
            print(two, "-", children_and_fathers[two])
    elif choice == "2":
        son_name = input("Введите имя ребенка: ")
        if son_name not in children_and_fathers:
            print("Отца с таким ребенком в базе нет.")
        else:
            print("Отец ребенка ", son_name, " это ", children_and_fathers[son_name], "!", sep="")
    elif choice == "3":
        son_name = input("Введите имя ребенка: ")
        father_name = input("Введите имя отца: ")
        if son_name not in children_and_fathers:
            children_and_fathers[son_name] = father_name
            print("Новая пара ребенок - отец добавлена.")
        else:
            print("Такой ребенок в базе уже существует.")
    elif choice == "4":
        son_name = input("Введите имя ребенка: ")
        father_name = input("Введите имя отца: ")
        father_name_new = input("Введите новое имя отца: ")
        if son_name not in children_and_fathers:
            print("Такой пары ребенок - отец в базе нет.")
        else:
            children_and_fathers.update({son_name: father_name_new})
            print("Замена произведена.")
    elif choice == "5":
        son_name = input("Введите имя ребенка: ")
        father_name = input("Введите имя отца: ")
        if son_name not in children_and_fathers:
            print("Такой пары ребенок - отец в базе нет.")
        else:
            del children_and_fathers[son_name]
            print("Такой пары ребенок - отец в базе больше нет.")
    else:
        print("Такого пункта в меню нет.")
input("Нажмите Enter, чтобы выйти.")