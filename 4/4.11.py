# Напишите проrрамму, которая принимала бы текст из попьзовательского ввода и печатала этот текст на экране
# наоборот.

word = input("Напечатайте свой текст: ")
number_word = len(word)
ney_word = ""
m = 0
for i in range(number_word):
    ney_word += word[m - 1]
    m -= 1
print("Ваш перевернутый текст:", ney_word)
