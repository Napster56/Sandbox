




products = [["Phone", 340, False],
            ["PC", 1420.95, False],
            ["Plant", 24.5, True],
            ["Bottle", 420.95, True]]

# print (products)

""" for loop version
on_sale_products = []
for product in products:
    if product[2]:        # if product is on sale
        on_sale_products.append(product)
print(on_sale_products)
"""


class Product:
    def __init__(self, name="", price="", is_on_sale=False):  # constructor method
        self.name = name                 # self is this particular object
        self.price = price               # name is a parameter stored in self
        self.is_on_sale = is_on_sale

    def __str__(self):
        on_sale_string = " (on sale!)" if self.is_on_sale else ""  # Ternery operator
        # if self.is_on_sale:                                      # replaces if statement
        #     on_sale_string = " (on sale!)"
        return "{} ${:.2f} {}".format(self.name, self.price, on_sale_string)

    def put_on_sale(self, discount):
        # discoun t is specified as a decimal, 0.31 = 31%
        self.is_on_sale = True
        self.price -= self.price * discount


# p = Product("Phone", 340)
# print(p)
# p2 = Product("Taco", 8.7, True)
# print(p2)
# print(p, type(p))   # prints object & type
# p.         # view methods & attributes available

# products = [Product("Phone", 200, False),
#             Product("PC", 1420.95, False),
#             Product("Plant", 24.5, True),
#             Product("Bottle", 420.95, True)]

def run_tests():
    p1 = Product("Phone", 340)
    p2 = Product("Taco", 908.7, True)
    print(p1, p2)
run_tests()

# for product in products:
#     print(product)
#
# products[0].put_on_sale(0.3)
# print(products[0])
#
# on_sale_products = [product.name for product in products if product.is_on_sale]
# print(on_sale_products)
