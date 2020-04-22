# Компьютерный датчик настроения
# Демонстрирует использование elif
import random
print("Я ощущаю ваашу энергетику. От моего экрана не скрыто ни одно из ваших чувств.")
print("Итак, ваше настроение...")
mood = random.randint(1, 4)
if mood == 1:
    # радость
    print(
        """
        -----------
        |           |
        |   O   O   |
        |      <    |
        |           |
        | .       . |
         |  `... ` |
           |_____|
        """
    )
elif mood == 2:
    # так себе
    print(
        """
        -----------
        |           |
        |   O   O   |
        |      <    |
        |           |
        |    ----   |
         |        |
           |_____|
        """
    )

elif mood == 3:
    # прескверное
    print(
        """
        -----------
        |           |
        |   O   O   |
        |      <    |
        |           |
        |   . ` .   |
         | `     ` |
           |______|
        """
    )
else:
    print("Небывает такого настроения! (Должно быть вы совершенно не в себе.)")
print("Но это только сегодня.")
input("\n\nНажмите Enter, чтобы выйти.")