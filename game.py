import random
from player import Player


class Game:
    POSSIBLE_COLORS = ("R", "G", "B", "C", "M", "Y")

    def __init__(self, player: Player, turn=0):
        self.secret_code = [random.choice(self.POSSIBLE_COLORS) for x in range(4)]
        self.turn = turn
        self.player = player

    def play(self):
        print("Welcome to the Mastermind game")
        print("The possible colors are: ", end="")
        print(", ".join(self.POSSIBLE_COLORS))
        print("Choose 4 of them and make your guess!")
        print(f"Turn {self.turn}")
        guesses = self.player.guess()
        
