"""
Program to create a FoodItem class which inherits from the Products class.
The subclass FoodItem extends the superclass Products.
"""

from products import Product


class FoodItem(Product):
    def __init__(self, name, price, is_on_sale, use_by_date):
        super().__init__(name, price, is_on_sale)
        self.use_by_date = use_by_date

    def __str__(self):
        return "{} {}".format(super().__str__(), self.use_by_date)


def run_tests():
    fi = FoodItem("Pine Nuts", 7.3, False, "13/07/2014")
    print(dir(fi))   # prints all the attributes from OBJECT


if __name__ == '__main__':
    run_tests()
