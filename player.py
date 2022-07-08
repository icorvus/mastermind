
class Player:

    def __init__(self, name):
        self.name = name

    def guess(self):
        guess_tab = []
        for _ in range(4):
            guess_tab.append(input(""))
        return guess_tab
