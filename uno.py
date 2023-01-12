import random

class Card:
    def __init__(self, color, value):
        self.color = color
        self.value = value
    def __str__(self):
        return f"{self.color} {self.value} card"

class UnoGame:
    def __init__(self):
        self.deck = [Card(color, value) for color in ["red", "green", "blue", "yellow"]
                     for value in range(1, 10)]
        self.deck += [Card(color, value) for color in ["red", "green", "blue", "yellow"]
                      for value in ["Skip", "Reverse", "Draw Two"]]
        self.deck += [Card("black", "Wild"), Card("black", "Wild Draw Four")]
        random.shuffle(self.deck)
        self.discard_pile = []
        self.players = []

    def play_game(self):
        self.discard_pile.append(self.deck.pop())
        while len(self.deck) > 0:
            for player in self.players:
                print(f"{player.name}'s turn:")
                print(f"Discard pile: {self.discard_pile[-1]}")
                # print(f"{player.name}'s hand: {player.hand}")
                print(f"{player.name}'s hand: ")
                for card in player.hand:
                    print(card)

                legal_plays = self.get_legal_plays(player)
                if len(legal_plays) == 0:
                    print(f"{player.name} has to draw a card.")
                    card = self.deck.pop()
                    player.hand.append(card)
                else:
                    # print(f"{player.name}'s legal plays: {legal_plays}")
                    print(f"{player.name}'s legal plays: ")
                    for card in legal_plays:
                        print(card)
                    play = input("Which card would you like to play? ")
                    while play not in legal_plays:
                        print("Invalid play. Please select a card from your hand.")
                        play = input("Which card would you like to play? ")
                    self.discard_pile.append(play)
                    player.hand.remove(play)
                    if len(player.hand) == 0:
                        print(f"{player.name} wins!")
                        return

    def get_legal_plays(self, player):
        legal_plays = [card for card in player.hand if card.color == self.discard_pile[-1].color or card.value == self.discard_pile[-1].value or card.color == "black"]
        return legal_plays

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
        for i in range(7):
            self.hand.append(game.deck.pop())

game = UnoGame()

player1 = Player("Player 1")
game.players.append(player1)
player2 = Player("Player 2")
game.players.append(player2)

game.play_game()
