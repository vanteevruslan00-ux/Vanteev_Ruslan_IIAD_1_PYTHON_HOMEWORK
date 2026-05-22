from classes.players import Player, ComputerPlayer
from classes.game import Game


def main():
    while True:
        print("Игра: Камень, Ножницы, Бумага")
        print("1 - Игрок против игрока")
        print("2 - Игрок против компьютера")

        mode = input("Выбери режим: ").strip()

        if mode == "1":
            player1 = Player("Игрок 1")
            player2 = Player("Игрок 2")
        else:
            player1 = Player("Игрок")
            player2 = ComputerPlayer("Компьютер")

        game = Game(player1, player2)
        game.play()


if __name__ == "__main__":
    main()