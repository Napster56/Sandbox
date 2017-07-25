"""
A list comprehension to produce a new list
containing only the products that are on sale
(True means it's on sale)
"""

products = [["Phone", 340, False], ["PC", 1420.95, True], ["Plant", 24.5, True]]

products_on_sale = [product for product in products if product[2] is True]   # is True is not needed
print(products_on_sale)


products_on_sale = [product for product in products if product[2]]
print(products_on_sale)