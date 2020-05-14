# Done
# I copied a big chunk of this from the Conway's Game of Life code from automate the boring stuff

import copy

WIDTH = 9
HEIGHT = 6

nextCells = []
for x in range(WIDTH):
    column = []  # Create a new column.
    for y in range(HEIGHT):
        if (x, y) in ((2, 0), (3, 0), (5, 0), (6, 0), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (1, 2),
                      (2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (2, 3), (3, 3), (4, 3), (5, 3), (6, 3), (3, 4),
                      (4, 4), (5, 4), (4, 5)):
            column.append('O')  # Add an 'O'.
        else:
            column.append('.')  # Add a '.'.
    nextCells.append(column)  # nextCells is a list of column lists.

while True:  # Main program loop.
    currentCells = copy.deepcopy(nextCells)

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[x][y], end='')  # Print the # or space.
        print()  # Print a newline at the end of the row.
    break
