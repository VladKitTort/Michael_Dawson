# Карты
# Демонстрирует сочетание объектов


class Card(object):
    """Одна игральная карта"""
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand(object):
    """ "Рука": набор карт на руках у одного игрока."""

    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = "<пусто>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


card_1 = Card(rank="A", suit="C")
print("\nВывожу на экран объект-карту")
print(card_1)
card_2 = Card(rank="2", suit="C")
card_3 = Card(rank="3", suit="C")
card_4 = Card(rank="4", suit="C")
card_5 = Card(rank="5", suit="C")
print("\nВывожу еще четыре карты: ")
print(card_2)
print(card_3)
print(card_4)
print(card_5)
my_hand = Hand()
print("\nПечатаю карты, которые у меня на руках до раздачи: ")
print(my_hand)
my_hand.add(card_1)
my_hand.add(card_2)
my_hand.add(card_3)
my_hand.add(card_4)
my_hand.add(card_5)
print("\nПечатаю пять карт, которые у меня на руках:")
print(my_hand)

your_hand = Hand()
my_hand.give(card_1, your_hand)
my_hand.give(card_2, your_hand)
print("\nПервые две из моих карт я передал вам.")
print("Теперь у вас на руках:")
print(your_hand)
print("А у меня на руках:")
print(my_hand)
my_hand.clear()
print("\nУменя на руках после того, как я сбросил все карты:")
print(my_hand)

input("\n\nНажмите Enter, чтобы выйти.")
