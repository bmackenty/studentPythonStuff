# this code was written by chatGPT
import random

# Define the ranks, suits, and values of cards
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
values = {'Ace': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'Jack': 10, 'Queen': 10, 'King': 10}

# Create a deck of cards
deck = []
for rank in ranks:
    for suit in suits:
        card = rank + ' of ' + suit
        deck.append(card)

# Shuffle the deck
random.shuffle(deck)

# Print the shuffled deck
for card in deck:
    print(card)
