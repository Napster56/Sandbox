
try:
    number = int(input("Enter a number"))
    print(10 / number)
except ValueError:
    print("Not a valid integer")
except ZeroDivisionError:
    print("Can't divide by zero")
except:
    print("Some other exception occurred")
print("Finished")
