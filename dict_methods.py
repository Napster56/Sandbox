d = {"boys": 3, "girls": 13}


# dict methods return dictionary views, not lists
print(d.keys())   # returns dict_keys(['boys', 'girls'])

print(d.values())   # returns dict_values([3, 13])

print(d.items())    # returns dict_items([('boys', 3), ('girls', 13)])

list(d.values()).sort()   # create a list, but it returns None

# Use sorted function tom sort a list and return a value
print(sorted(list(d.values())))    # returns [3, 13]

print(d.get("boys", 0))    # returns 3; default value is 0
print(d.get("men", 0))    # returns 0; default value is 0
