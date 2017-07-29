"""
Rename files in a directory by replacing text
"""

import os

FROM_TEXT = "text to change"
TO_TEXT = "change to XXX"
DIRECTORY = "file path"

os.chdir(DIRECTORY)
for filename in os.listdir('.'):
    # print(filename)
    if FROM_TEXT in filename:
        new_name = filename.replace(FROM_TEXT, TO_TEXT)
        # os.rename(filename, new_name)      # check new_name before replacing!!!
        print(new_name)
