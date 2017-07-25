"""
Program to create a User class for the Hey Taco simulation
"""
STARTING_TACOS = 5


class User:
    def __init__(self, name):
        self.name = name
        self.tacos = STARTING_TACOS
        self.score = 0

    def __str__(self):
        return "{self.name} has {self.tacos} tacos left. Score: {self.score}".format(self=self)

    def give_taco(self, other_user, number_of_tacos):
        if number_of_tacos > self.tacos:
            number_of_tacos = self.tacos
        self.tacos -= number_of_tacos
        other_user.score += number_of_tacos


def run_tests():
    user1 = User("Lindsay")
    user2 = User("Jeff")
    print(user1)
    print(user2)
    user1.give_taco(user2, 13)
    print(user1)
    print(user2)

if __name__ == '__main__':
    run_tests()
