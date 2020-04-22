# Создайте программу, которая будет выводить список слов в случайном порядке.
# На экране должны печататься без повторений все слова из представленного списка.
#
import random
WORDS = ["скот", "слон", "поле", "локоть", "саламандра", "санта клаус", "кит", "фура"]
word = []
word += WORDS
print(word)
while word:
    position = random.randrange(len(word))
    print(word[position])
    word = word[:position] + word[(position + 1):]
print(WORDS)
print(word)