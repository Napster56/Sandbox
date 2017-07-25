numbers = [1, 2, 3, 4]

values = [n for n in numbers[::2]]   # iterates thru numbers, collects n
print(values)

values = [n * 2 for n in numbers]   # iterates thru numbers, collects n * 2
print(values)

values = [str(n * 2) for n in numbers]   # iterates thru numbers, collects n * 2 as strings
print(values)

numbers.append(8)    # sppend takes one argument
numbers.append(12)

values = tuple([n for n in numbers if n % 2 == 0])   # iterates thru numbers, collects n if even
print(values)

uppers = [c for c in "Hi There Mom" if c.isupper()]
print(uppers)