# Обработаем
# Демонстрирует обработку исключительных ситуаций
# try/except
try:
    num = float(input("Введите число: "))
except:
    print("Похоже, это не число!")

try:
    num = float(input("Введите число: "))
except ValueError:
    print("Похоже, это не число!")

# Обработка исключений нескольких разных типов
print()
for value in (None, "Привет!", 11):
    try:
        print("Пытаюсь преобразовать в число: ", value, "-->", end=" ")
        print(float(value))
    except (TypeError, ValueError):
        print("Похоже это не число!")

print()
for value in (None, "Привет!", 11):
    try:
        print("Пытаюсь преобразовать в число: ", value, "-->", end=" ")
        print(float(value))
    except TypeError:
        print("Я умею преобразовывать только строки и числа!")
    except ValueError:
        print("Я умея преобразовывать только строки, составленные из цифр!")

try:
    num = float(input("\nВведите число: "))
except ValueError as e:
    print("Это не число! Интерпритатор как бы говорит нам:")
    print(e)

# try/except/else
try:
    num = float(input("\nВведите число: "))
except ValueError:
    print("Это не число!")
else:
    print("Вы ввели число:", num)
input("\n\nНажмите Enter, чтобы выйти.")