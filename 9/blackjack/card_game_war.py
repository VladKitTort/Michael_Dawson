# Карточная игра "Война"
# От 1 до 7 игроков
import cards
import games


class W_Card(cards.Card):
    """Карта для игры в "Война"."""

    ACE_VALUE = 1

    @property
    def value(self):
        v = W_Card.RANKS.index(self.rank) + 1
        return v


class W_Deck(cards.Deck):
    """Колода для игры в "Война"."""

    def populate(self):
        for suit in W_Card.SUITS:
            for rank in W_Card.RANKS:
                self.cards.append(W_Card(rank, suit))


class W_Hand(cards.Hand):
    """"Рука": набор карт "Блек-джека" у одного игрока."""

    def __init__(self, name):
        super(W_Hand, self).__init__()
        self.name = name

    def __str__(self):
        rep = f"{self.name}:    {super(W_Hand, self).__str__()}"
        if self.total:
            rep += f"{self.total}"
        return rep

    @property
    def total(self):
        # если у одной из карт value равно None, то и все свойства равно None
        for card in self.cards:
            if not card.value:
                return None
            t = 0
            for playing_card in self.cards:
                t += playing_card.value
            return t


class W_Player(W_Hand):
    """Игрок в "Война" """

    def lose(self):
        print(f"{self.name} проиграл.")

    def win(self):
        print(f"{self.name} выиграл.")

    def push(self):
        print(f"{self.name} сыграли в ничью.")


class W_Game:
    """Игра в Блек-джек"""

    def __init__(self, names):
        self.players = []
        for name in names:
            player = W_Player(name)
            self.players.append(player)
        self.deck = W_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            sp.append(player)
        return sp

    def winner(self, players):
        # сравниваем суммы очков у игроков
        win = [players[0]]
        for i in range(len(players) - 1):
            if win[0].total < players[i + 1].total:
                win[0] = players[i + 1]
            elif win[0].total == players[i + 1].total:
                win.append(players[i + 1])
        for i in range(len(win)):
            print(f"{win[i].name} - выиграл!")

    def play(self):
        self.deck.populate()
        self.deck.shuffle()
        # сдача всем по 1 карте
        self.deck.deal(self.players, per_hand=1)
        n = []
        for player in self.players:
            n.append(player)
            print(player)
        self.winner(n)
        # удаление всех карт
        for player in self.players:
            player.clear()


def main():
    print("\t\tДобро пожаловать за игровой стол Блек-джека!\n")
    names = []
    number = games.ask_number("Сколько всего игроков? (2-7): ", low=2, high=8)
    for i in range(number):
        name = input("Введите имя игрока: ")
        names.append(name.title())
        print()
    game = W_Game(names)
    again = None
    while again != "n":
        game.play()
        again = games.ask_yes_no("\nХотите сыграть еще раз? ")


main()
input("\n\nНажмите Enter, чтобы выйти.")
