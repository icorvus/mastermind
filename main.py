from game import Game
from player import Player


def main():
    player1 = Player("Wiki")
    game1 = Game(player1)
    game1.play()


if __name__ == "__main__":
    main()
