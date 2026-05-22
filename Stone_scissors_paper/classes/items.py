class Item:
    def __init__(self, name):
        self.name = name

    def beats(self, other):
        return False

    def __str__(self):
        return self.name


class Rock(Item):
    def __init__(self):
        super().__init__("Камень")

    def beats(self, other):
        return isinstance(other, Scissors)


class Scissors(Item):
    def __init__(self):
        super().__init__("Ножницы")

    def beats(self, other):
        return isinstance(other, Paper)


class Paper(Item):
    def __init__(self):
        super().__init__("Бумага")

    def beats(self, other):
        return isinstance(other, Rock)