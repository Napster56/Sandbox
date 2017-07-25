
phonebook = {}    # creates an empty dictionary
print(type(phonebook))

phonebook["Bill"] = '12345'  # creates a key-value pair
phonebook["Ada"] = '61234'
phonebook["Ada"] = '0001'    # modifies key "Ada"
# phonebook["Gary"] += '22345'  # causes KeyError because "Gary" not in dict

print(phonebook)

people_counts = {"boys": 0, "girls": 0}   # create dict with initial values = 0

"""
choice = input("Gender: (g/b), - to stop")
while choice != "-":
    if choice == "b":
        people_counts["boys"] += 1
    elif choice == "g":
        people_counts["girls"]
        += 1
    choice = input("Gender: (g/b, - to stop")
"""
people_counts = {"boys": 3, "girls": 13}

# print(people_counts)
print("Boys: {}, Girls: {}".format(people_counts["boys"], people_counts["girls"]))

# loop thru dict and get the key & it's value
for gender in people_counts:
    print("{:5} - {:4}".format(gender, people_counts[gender]))

for gender, count in people_counts.items():   # items method for dict
    print("{:5} - {:4}".format(gender, count))



# check programming patterns in CP1404 Github

