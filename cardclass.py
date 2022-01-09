import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_names = {
            1 : "Ace",
            2 : "Two",
            3 : "Three",
            4 : "Four",
            5 : "Five",
            6 : "Six",
            7 : "Seven",
            8 : "Eight",
            9 : "Nine",
            10 : "Ten",
            11 : "Jack",
            12 : "Queen",
            13 : "King"
        }

        self.suit_names = {
            "d" : "Diamonds",
            "c" : "Clubs",
            "h" : "Hearts",
            "s" : "Spades"
        }

    def get_rank(self):
        return self.rank_names[self.rank]

    def get_suit(self):
        return self.suit_names[self.suit]

    def value(self):
        if self.rank in range(1,9):
            return self.rank
        else:
            return 10

    def __str__(self):
        return f"{self.get_rank()} of {self.get_suit()}"


def create_card(n):
    for i in range(n):
        x = random.randint(1,13)
        choices = ("d","c","h","s")
        y = random.choice(choices)
        card = Card(x,y)
        print(card)
        print("-----------------")

def test_card():
    x = random.randint(1,13)
    choices = ("d","c","h","s")
    y = random.choice(choices)
    card = Card(x,y)

    print(f"Card Rank: {card.get_rank()}")
    print("-----------------")
    print(f"Card Suit: {card.get_suit()}")
    print("-----------------")
    print(f"Card Blackjack value: {card.value()}")
    print("-----------------")
    print(card)
    print("-----------------")

create_card(4)
test_card()