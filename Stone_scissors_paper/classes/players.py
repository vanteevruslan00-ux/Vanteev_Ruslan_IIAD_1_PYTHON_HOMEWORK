import random
from classes.items import Rock, Scissors, Paper


class Player:
    def __init__(self, name):
        self.name = name
        self.item = None

    def choose_item(self):
        choice = input(
            f"{self.name}, выбери предмет (камень (1) / ножницы(2) / бумага (3)): "
        ).strip().lower()

        if choice == ("1" or "камень"):
            self.item = Rock()
        elif choice == ("2" or "ножницы"):
            self.item = Scissors()
        elif choice == ("3" or "бумага"):
            self.item = Paper()
        else:
            print("Неверный ввод. Выбери заново.")
            Player.choose_item(self)


class ComputerPlayer(Player):
    def choose_item(self):
        self.item = random.choice([Rock(), Scissors(), Paper()])