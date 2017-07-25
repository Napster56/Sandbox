"""
Program prompts the user for a name and age,
add these to the dictionary, then display all of the data nicely.
"""
"""
ages_dict = {"Bill": 21, "Jane": 34, "Jack": 56}

print(ages_dict["Bill"])           # prints 21
# print(ages_dict["Bob"])          # returns KeyError: 'Bob'

# get method prevents a KeyError if user enters key not in dict
print(ages_dict.get("Bob", 0))     # prints 0 but doesn"t error

ages_dict["Bob"] = ages_dict.get("Bob", 0) + 1  # sets age to 1 more than previous age
print(ages_dict.get("Bob"))           # returns 1
print(ages_dict)      # prints {'Bill': 21, 'Jack': 56, 'Jane': 34, 'Bob': 1}



name = input("Enter name: ")
age = input("Enter age: ")

ages_dict[name] = age        # set a new value into dict
# iterate thru dict
for name, age in ages_dict.items():
    print("{:10} - {:2}".format(name, age))
"""

ages_dict = {"Bill": 17, "Jane": 34, "Jack": 56, "Sven": 13}

new_ones = {name: age for name, age in ages_dict.items() if age < 18}
print(new_ones)
