#!/usr/bin/env python3

import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')  # noqa: E501
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}  # noqa: E501


class Card():
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + " of " + self.suite


class Deck():
    def __init__(self):
        self.all_cards = []

        for suit in suits:
            for rank in ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


class Player():
    def __init__(self, name):
        self.name = name
        self.all_cards = []

    def remove_one(self):
        return self.all_cards.pop(0)

    def add_cards(self, new_cards):
        # if type(new_cards) == type([]):
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)

    def __str__(self):
        return "Player {} has {} cards.".format(self.name, len(self.all_cards))


# Game Logic
# Game Setup
# Setup Players

player_one = Player("Juan")
player_two = Player("Eduardo")

# Create Deck and shuffle
new_deck = Deck()
new_deck.shuffle()

# Deal cards to Players
for x in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())


# Setup Game
game_on = True

round_num = 0

while game_on:
    round_num += 1
    print("Round {}".format(round_num))

    if len(player_one.all_cards) == 0:
        print("Player one, out of cards! Player Two Wins!")
        game_on = False
        break
    if len(player_two.all_cards) == 0:
        print("Player two, out of cards! Player One Wins!")
        game_on = False
        break

    # Start new round
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())

    at_war = True

    while at_war:
        if player_one_cards[-1].value > player_two_cards[-1].value:
            player_one.add_cards(player_one_cards)
            player_one.add_cards(player_two_cards)

            at_war = False

        elif player_one_cards[-1].value < player_two_cards[-1].value:
            player_two.add_cards(player_one_cards)
            player_two.add_cards(player_two_cards)

            at_war = False

        else:
            print("WAR!!")

            if len(player_one.all_cards) < 5:
                print("Player One unable to declare war")
                print("PLAYER TWO WINS!")
                game_on = False
                break

            if len(player_two.all_cards) < 5:
                print("Player Two unable to declare war")
                print("PLAYER One WINS!")
                game_on = False
                break

            else:
                for num in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
