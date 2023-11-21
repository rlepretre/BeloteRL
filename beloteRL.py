SUITS = ["Heart", "Spades", "Diamond", "Club"]
VALUES = ["A","7","8","9","10","J","Q","K"]

import random


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_card(self, card_index):
        return self.hand.pop(card_index)
    
    def show_hand(self):
        print("The hand of {} is :".format(self.name))
        for c in self.hand:
            c.show()
        print("--------------")

    def pickup_trump(self, trump):
        self.hand.append(trump)


class Game:
    def __init__(self, players):
        self.players = players
        self.deck = []
        self.trump = ""
        for suit in SUITS:
            for val in VALUES:
                card = Card(suit, val)
                self.deck.append(card)

    def show_deck(self):
        print("These are currently in the deck:")
        for c in self.deck:
            c.show()
        print("---------------")

    def shuffle_deck(self):
        random.shuffle(self.deck)

    def deal_first_hand(self):
        for p in self.players:
            for i in range(5):
                p.hand.append(self.deck.pop())

    def pick_trump_phase(self):
        if True : # agent.pick_trump()
            trump_card = self.deck.pop()
            player1.pickup_trump(trump_card)
            self.trump = trump_card.suit
        if False : # agent.pick_trump()
            trump_card = self.deck.pop()
            player2.pickup_trump(trump_card)
            self.trump = trump_card.suit
        if False : # agent.pick_trump()
            trump_card = self.deck.pop()
            player3.pickup_trump(trump_card)
            self.trump = trump_card.suit
        if False : # agent.pick_trump()
            trump_card = self.deck.pop()
            player4.pickup_trump(trump_card)
            self.trump = trump_card.suit


class Card:
    def __init__(self, suit, val):
        self.suit = suit
        self.val = val

    def show(self) :
        print ("{} of {}".format(self.val , self.suit))




player1 = Player("Jaspy")
player2 = Player("Lucas")
player3 = Player("Lio")
player4 = Player("Rom")

my_game = Game([player1, player2, player3, player4])
my_game.shuffle_deck()
my_game.deal_first_hand()


player1.show_hand()
player2.show_hand()
player3.show_hand()
player4.show_hand()

my_game.show_deck()
