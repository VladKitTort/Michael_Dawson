# Арсенал героя
# Демонстрирует создание кортежа
# Создадим пустой кортеж
inventory = ()
#рассмотрим его как условие
if not inventory:
    print("Вы безоружны.")
input("\nНажмите Enter, чтобы продолжить.")
#теперь создадим кортеж с несколькими элементами
inventory = ("меч",
             "кольчуга",
             "щит",
             "целебное снадобье")
#выведим этот кортеж на экран
print("\nСодержимое кортежа:")
print(inventory)
# выведим все элементы последовательно
print("\nИтак, в вашем арсенале:")
for item in inventory:
    print(item)
input("\n\nНажмите Enter, чтобы выйти.")