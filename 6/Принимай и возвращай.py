# Принимай и возвращай
# Демонстрирует параметры и возвращаемые элементы
def display(message):
    print(message)
def give_me_five():
    five = 5
    return five
def ask_yes_no(question):
    """Задает вопрос с ответом "да" или "нет"."""
    response = None
    while response not in ("y", "n"):
        response = input(question).lower()
    return response
# основная часть
display("Вам сообщение.\n")
number = give_me_five()
print("Вот что возвратилаа функция give_me_five():", number)
ansver = ask_yes_no("\nПожалуйста, введите \"у\" или \"n\": ")
print("Спасибо, что ввели", ansver)
input("\n\nНажмите Enter, чтобы выйти.")