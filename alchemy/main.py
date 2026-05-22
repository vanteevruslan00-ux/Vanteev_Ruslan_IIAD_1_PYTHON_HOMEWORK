# Вантеев Руслан ИИАД_1
class Element:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class AlchemyGame:

    def __init__(self):
        self.elements = {}
        self.recipes = {}

        self._add_element("Вода")
        self._add_element("Огонь")
        self._add_element("Земля")
        self._add_element("Воздух")

        self._init_recipes()

    def _add_element(self, name):
        if name not in self.elements:
            self.elements[name] = Element(name)
            return True
        return False

    def _add_recipe(self, a, b, result):
        self._add_element(a)
        self._add_element(b)
        self.recipes[(a, b)] = result
        self.recipes[(b, a)] = result

    def _init_recipes(self):
        self._add_recipe("Вода", "Огонь", "Пар")
        self._add_recipe("Земля", "Огонь", "Лава")
        self._add_recipe("Воздух", "Огонь", "Энергия")
        self._add_recipe("Вода", "Земля", "Грязь")
        self._add_recipe("Вода", "Воздух", "Туман")
        self._add_recipe("Земля", "Воздух", "Пыль")

    def mix(self, first, second):
        print(f"\nПробуем смешать: {first} + {second}")

        if first not in self.elements:
            print(f"Элемент '{first}' ещё не создан")
            return None
        if second not in self.elements:
            print(f"Элемент '{second}' ещё не создан")
            return None

        pair = (first, second)
        if pair in self.recipes:
            result_name = self.recipes[pair]

            if result_name in self.elements:
                print(f"Получился {result_name} (уже есть)")
            else:
                self.elements[result_name] = Element(result_name)
                print(f"ПОЛУЧЕН НОВЫЙ ЭЛЕМЕНТ: {result_name}")
            return result_name
        else:
            print(f"Ничего не получилось...")
            return None

    def show_all(self):
        print("СОЗДАННЫЕ ЭЛЕМЕНТЫ:")
        for name in sorted(self.elements.keys()):
            print(f"  * {name}")
        print(f"\nВсего: {len(self.elements)} элементов")


if __name__ == "__main__":
    print("АЛХИМИЯ\n")

    game = AlchemyGame()
    game.show_all()

    print("\nСмешиваем элементы")

    game.mix("Вода", "Огонь")
    game.mix("Огонь", "Земля")
    game.mix("Воздух", "Огонь")
    game.mix("Вода", "Земля")
    game.mix("Вода", "Воздух")
    game.mix("Земля", "Воздух")

    print("\nСмешиваем новые элементы")

    game.mix("Пар", "Вода")
    game.mix("Лава", "Воздух")
    game.mix("Энергия", "Вода")

    print("\nПовторяем рецепт")
    game.mix("Вода", "Огонь")

    game.show_all()