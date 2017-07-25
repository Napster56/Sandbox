"""
Program to create a 6 x 6 crossword
"""

crosswordPuzzle = []
row_count = 6
col_count = 6

# nested iteration
for i in range(row_count):               # nested iteration
    row = []
    for j in range(col_count):
        row += ['?']
    crosswordPuzzle.append(row)
for row in crosswordPuzzle:              # display in a matrix
    for col in row:
        print(col, end='')
    crosswordPuzzle[0][0] = 'T'
    crosswordPuzzle[1][1] = 'Y'
    crosswordPuzzle[2][2] = 'R'
    crosswordPuzzle[3][3] = 'O'
    crosswordPuzzle[4][4] = 'N'
    crosswordPuzzle[5][5] = 'E'
    print()




