from drink import Drink


class DrinkList:
    def __init__(self):
        self.drinks = []

    def __str__(self):
        return str([str(drink) for drink in self.drinks])

    def __len__(self):
        return len(self.drinks)

    def add(self, drink):
        self.drinks.append(drink)

    def get_number_alcoholic(self):
        return len([1 for drink in self.drinks if drink.is_alcoholic()])

    """ return sum([])         # replaced by above list comprehension
        count = 0
        for drink in self.drinks:
            if drink.is_alcoholic():
                count += 1
        return count """

    def get_alcohol_volume(self):
        return sum([drink.get_alcohol_volume() for drink in self.drinks])

    def get_total_price(self):
        return sum([drink.price for drink in self.drinks])


# Suggest putting tests in a separate tests_file
def run_tests():  # DO NOT pass a List into function because it is mutable!!!
    d = DrinkList()
    drink1 = Drink("Pina Colada", 12.3, 450, 12.5)
    drink2 = Drink("Coffee", 4.5, 280, 0)
    d.add(drink1)
    d.add(drink1)
    d.add(drink2)
    print(d)
    print(d.get_number_alcoholic())
    print(d.get_alcohol_volume())


if __name__ == '__main__':
    run_tests()
