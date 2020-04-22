# Только согласные
# Демонстрирует, как создавать новые строки из исходных с помощью цикла for
message = input("Введите текст: ")
new_message = ""
vowels = "aeiouаеёиоуыэюя"
print()
for i in message:
    if i.lower() not in vowels:
        new_message += i
        print("Сщздана новая строка: ", new_message)
print("\nВот ваш текст с изъятыми гласными буквами: ", new_message)
input("\n\nНажмите Enter, тобы выйти.")