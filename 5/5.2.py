# Рекорды
# Демонстрирует списочные методы.
scores = []
choice = None
while choice != "0":
    print(
        """
        Рекорды
        0 - Выйти.
        1 - Показать рекорды.
        2 - Добавить рекорд.
        3 - Удалить рекорд.
        4 - Сортировать список.
        """
    )
    choice = input("Ваш выбор: ")
    if choice == "0":
        print("До свидания.")

    # Вывод рекордов на экран.
    elif choice == "1":
        if not scores:
            print("Рекордов еще нет.")
        else:
            print("Рекорды:")
            for score in scores:
                print(score)
        input("\nHaжмитe Enter, чтобы продолжить.")
    elif choice == "2":
        score = int(input("Введите свой рекорд: "))
        scores.append(score)
        print("Рекорд добавлен.\n")
        input("\nHaжмитe Enter, чтобы продолжить.")
    elif choice == "3":
        score = int(input("Какой из рекордов удалить?: "))
        if score in scores:
            scores.remove(score)
            print("Рекорд", score, "был удален.")
        else:
            print("Результат", score, "не содержится в спске рекордов.")
        input("\nHaжмитe Enter, чтобы продолжить.")
    # Сортировка рекордов.
    elif choice == "4":
        scores.sort(reverse=True)
        print("Рекорды отсортированы.")
        input("\nHaжмитe Enter, чтобы продолжить.")
    else:
        print("Извините, в меняю нет пункта ", "\"", choice, "\".", sep="")
input("\n\nHaжмитe Enter, чтобы выйти.")
