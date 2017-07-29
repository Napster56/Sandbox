""" OS demos """

import os

# result = os.system("dir")      # Displays a list of a folder's files and subfolders
# print(result)


# displays the current working directory which is the top level of Project running
print(os.getcwd())

# list contents of current directory, indicated by "."
print(os.listdir("."))

# list contents at a particular path
print(os.listdir("Kivy demos"))

# change to new path
os. chdir("C:")

os.chdir("G:\CP1404 Programming I\Sandbox")

for filename in os.listdir('.'):
    # print(filename)
    if filename.endswith('.py'):
        # print(filename)
        # with open(filename) as python_file
        with open(filename) as f:
            if "def " in f.read():    # include a space
                print(filename)





