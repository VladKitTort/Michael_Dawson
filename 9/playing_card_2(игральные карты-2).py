# Карты 2.0
# Демонстрирует расширение класса через наследование


class Card(object):
    """Одна игральная карта."""

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
                rep += f"{card}\t"
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


class Deck(Hand):
    """Колода игральных карт."""

    def populate(self):
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[-1]
                    self.give(top_card, hand)
                else:
                    print("Не могу больше сдавать: карты закончились!")


# основная часть
deck_1 = Deck()
print("Создана новая колода")
print("Вот эта колода")
print(deck_1)
deck_1.populate()
print("\nВ колоде появились карты.")
print("Вот как она выглядит сейчас: ")
print(deck_1)
deck_1.shuffle()
print(deck_1)
my_hand = Hand()
your_hand = Hand()
hands = [my_hand, your_hand]
deck_1.deal(hands, per_hand=5)
print("\nМне и вам на руи роздано по 5 карт.")
print("У меня на руках:")
print(my_hand)
print("У вас на руках:")
print(your_hand)
print("Осталось в колоде")
print(deck_1)
deck_1.clear()
print(f"Вот как она выглядит теперь: {deck_1}")

input("\n\nНажмите Enter, чтобы выйти.")