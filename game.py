import random


class Game:
    POSSIBLE_COLORS = ["R", "G", "B", "C", "M", "Y"]

    def __init__(self):
        self.secret_code = [random.choice(self.POSSIBLE_COLORS) for x in range(4)]
