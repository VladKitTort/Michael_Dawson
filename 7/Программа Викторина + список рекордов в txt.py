# Викторина + номинал + список рекордов + в .txt
# Игра на выбор правильного варианта ответа
# Вопросы которые читаются из файла
import sys


def open_file(file_name, mode):
    """Открывает файл."""
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print("Не возможно открыть файл", file_name, ", Работа программы будет завершина.\n", e)
        input("\n\nНажмите Enter, чтобы выйти.")
        sys.exit()
    else:
        return the_file


def record_file(file_name, mode):
    """Открывает файл."""
    try:
        the_file = open(file_name, mode, encoding='utf-8')
    except IOError as e:
        print("Не возможно открыть файл", file_name, ", Работа программы будет завершина.\n", e)
        input("\n\nНажмите Enter, чтобы выйти.")
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    """Возвращает в отформатированном виде очередную строку игрового файла."""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line


def next_block(the_file):
    """Возвращает очередной блок данных из игрового файла."""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)
    par = next_line(the_file)
    return category, question, answers, correct, explanation, par


def welcome(title):
    """Приветствие игрока и сообщает тему игры."""
    print("\t\tДобро пожаловать в игру \"Викторина\"!")
    print("\t\t", title, "\n")


def main():
    trivia_file = open_file("trivia_par.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    points = 0
    # Извлечение первого блока.
    category, question, answers, correct, explanation, par = next_block(trivia_file)
    while category:
        # Вывод вопроса на экран
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])
        # Получение ответа
        answer = input("Ваш ответ: ")
        # Проверка ответа
        if answer == correct:
            print("\nДА!", end=" ")
            score += 1
            points += int(par)
        else:
            print("\nНет.", end=" ")
        print("Правильный ответ:", correct, "\n", explanation)
        print("Счет:", score)
        print("Количество баллов:", points, "\n\n")
        category, question, answers, correct, explanation, par = next_block(trivia_file)
    trivia_file.close()
    print("Это был последний вопрос!")
    print("На вашем счету:\nПравельных ответов", score, "\nКоличество баллов:", points)
    name = input("Введите  ваше имя: ")
    points = str(points)
    record = name + ":" + points
    trivia_par_file = record_file("trivia_points.txt", "a")
    trivia_par_file.write(record)
    trivia_par_file.close()


main()
input("\n\nНажмите Enter, чтобы выйти.")