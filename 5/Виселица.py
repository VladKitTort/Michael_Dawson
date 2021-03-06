# Виселица.
#
# Классическая игра виселица. Компьютер случайным образом выбирает слово,
# которое игрок должен отгадать буква за буквой. Если игрок не сумеет
# отгадать за отведенное количество попыток, на экране появится фигурка повешанного.
#
# Импорт модуля
import random

HANGMAN = (
    """
     ---------
     |       |
     |       |
     |
     |
     |
     |
     |
     |
     |
     |
    ------------
    """,
    """
     ---------
     |       |
     |       |
     |       O      |
     |
     |
     |
     |
     |
     |
     |
    ------------
    """,
    """
     ---------
     |       |
     |       |
     |       O      |   -+-
     |
     |
     |
     |
     |
     |
     |
    ------------
    """,
    """
     ---------
     |       |
     |       |
     |       O      |   /-+-
     |
     |
     |
     |
     |
     |
     |
    ------------
    """,
    """
     ---------
     |       |
     |       |
     |       O      |   /-+-/
     |
     |
     |
     |
     |
     |
     |
    ------------
    """,
    """
     ---------
     |       |
     |       |
     |       0      |   /-+-/
     |       |
     |       |
     |
     |
     |
     |
     |
    ------------
    """,
    """
     ---------
     |       |
     |       |
     |       0      |   /-+-/
     |       |
     |       |
     |      | 
     |      |
     |
     |
     |
    ------------
    """,
    """
     ---------
     |       |
     |       |
     |       0      |   /-+-/
     |       |
     |       |
     |      | |
     |      | |
     |
     |
     |
    ------------
    """
)
MAX_WRONG = len(HANGMAN) - 1
WORDS = ("OVERUSED", "CLAM", "GUAM", "TAFFETA", "PYTHON")

# Инициализация переменных
word = random.choice(WORDS)     # слово для отгадывания
so_far = "-" * len(word)        # по одному дефису на каждую букву, которую нужно отгадать
wrong = 0       # оличество ошибок которые сделал игрок
used = []       # буквы которые игрк уже предлогал

print("Добро пожаловать в игру \"Виселица\"! Удачи вам.")
while wrong < MAX_WRONG and so_far != word:
    print(HANGMAN[wrong])
    print("\nВы уже предлогали следующие буквы:\n", used)
    print("\nОтгаданное вами в слове сейчас выглядит так:\n", so_far)
    guess = input("\n\nВведите букву: ")
    guess = guess.upper()
    while guess in used:
        print("Вы уже пробовали букву:", guess)
        guess = input("\n\nВведите букву: ")
        guess = guess.upper()
    used.append(guess)
    if guess in word:
        print("\nДа! Буква", guess, "есть в загаданном слове!")
        # Новая строка so_far с отгаданной буквой или буквами
        new = ""
        for i in range(len(word)):
            if guess == word[i]:
                new += guess
            else:
                new += so_far[i]
        so_far = new
    else:
        print("\nК  сожалению, буквы", guess, "нет в загаданном слове.")
        wrong += 1
    if wrong == MAX_WRONG:
        print(HANGMAN[wrong])
        print("\nВас повесили.")
    else:
        print("\nВы выиграли!")
print("\nБыло загаданно слово", word)
input("\nНажмите Enter, чтобы выйти.")
