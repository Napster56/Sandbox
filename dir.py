class MyClass():
    pass

my_class = type(MyClass)
print(my_class)

my_class = dir(MyClass)

print(my_class)

my_instance = MyClass()
my_instance = dir(my_instance)
print(my_instance)

my_inst = type(my_instance)
print(my_inst)
