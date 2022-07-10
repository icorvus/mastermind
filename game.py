import random
from player import Player


class Game:
    POSSIBLE_COLORS = ("R", "G", "B", "C", "M", "Y")

    def __init__(self, player: Player, turn=0):
        self.secret_code = self.generate_secret_code()
        self.turn = turn
        self.player = player

    def play(self):
        print("Welcome to the Mastermind game")
        print("The possible colors are: ", end="")
        print(", ".join(self.POSSIBLE_COLORS))
        print("Choose 4 of them and make your guess!")
        print("You have only 12 turns to do it!")
        print(f"Turn {self.turn}")
        guesses = self.player.guess()
        self.check_guesses(guesses)
        print(self.secret_code)

    def check_guesses(self, guesses):
        exact_guesses = 0
        good_color_guesses = 0
        for i, guess in enumerate(guesses):
            if guess in self.secret_code:
                good_color_guesses += 1
                if i == self.secret_code.index(guess):
                    exact_guesses += 1
        good_color_guesses -= exact_guesses
        return exact_guesses, good_color_guesses

    @classmethod
    def generate_secret_code(cls):
        possible_colors = list(cls.POSSIBLE_COLORS)
        secret_code = []
        for _ in range(4):
            color_choice = random.choice(possible_colors)
            secret_code.append(color_choice)
            possible_colors.remove(color_choice)
        return secret_code
