"""
Create a class for a consumer credit card
"""


class CreditCard:

    def __init__(self, customer, bank, account, limit):
        """Make a new credit card instance

        The initial balance is zero.
        """
        self.customer = customer
        self.bank = bank
        self.account = account
        self.limit = limit
        self.balance = 0

    def get_customer(self):
        """Return the name of the customer"""
        return self.customer

    def get_bank(self):
        """Return the bank's name"""
        return self.bank

    def get_account(self):
        """Return the card id number"""
        return self.account

    def get_limit(self):
        """Return credit limit"""
        return self.limit

    def get_balance(self):
        """Return the current balance"""
        return self.balance

    def debit_card(self, price):
        """Charge price to the card, if sufficient credit limit
            Return True if charge was processed; False if charge denied
        """

        if price + self.balance > self.limit:
            return False
        else:
            self.balance += price
            return True

    def make_payment(self, amount):
        """Process customer payment to reduce balance"""
        self.balance -= amount

    def __str__(self):
        return "Customer = {}, Bank = {}, Account = {}, Balance = {}, Limit = {}".format(self.customer, self.bank,
                                                                                         self.account, self.account, self.limit)

Joe = CreditCard("Jeff", "ANZ", "555 555", 2500)
print(Joe)



if __name__ == '__main__':
    wallet = []
    wallet.append(CreditCard("John Doe", "CBA", "5391 0375 9387 5309", 1000))
    wallet.append(CreditCard("John Doe", "NAB", "3485 0399 3395 1954", 3500))
    wallet.append(CreditCard("John Doe", "Westpac", "2248 1362 0477 3900", 5500))

    for i in range(1, 55):
        wallet[0].debit_card(i)
        wallet[1].debit_card(2 * i)
        wallet[2].debit_card(3 * i)

    for i in range(3):
        print(("Customer =", wallet[i].get_customer()))
        print(("Bank =", wallet[i].get_bank()))
        print(("Account =", wallet[i].get_account()))
        print(("Balance =", wallet[i].get_balance()))
        print(("Limit =", wallet[i].get_limit()))
        while wallet[i].get_balance() > 500:
            wallet[i].make_payment(500)
            print(("New balance =", wallet[i].get_balance()))
        print()

