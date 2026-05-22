import sys

class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def play(self):
        self.player1.choose_item()
        self.player2.choose_item()

        print(f"\n{self.player1.name} выбрал: {self.player1.item}")
        print(f"{self.player2.name} выбрал: {self.player2.item}")

        if type(self.player1.item) == type(self.player2.item):
            print("Ничья!")
            print("Продолжить?")
            chouse = input("Да(1) или нет(0):  ")
            if chouse == "0" or "нет":
                sys.exit()


        elif self.player1.item.beats(self.player2.item):
            print(f"Победил {self.player1.name}!")
            print("Продолжить?")
            chouse = input("Да(1) или нет(0):  ")
            if chouse == "0" or "нет":
                sys.exit()
        else:
            print(f"Победил {self.player2.name}!")
            print("Продолжить?")
            chouse = input("Да(1) или нет(0):  ")
            if chouse == "0" or "нет":
                sys.exit()
