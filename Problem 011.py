# Problem 11
# What is the greatest product of four adjacent numbers in the same direction (up, down, left, right, or diagonally)
# in the 20×20 grid?

import time


def main():
    # Create the grid
    grid = prepare_grid()

    # Set the greatest product
    greatest_product = 0

    # Check horizontals
    for i in range(0, 20):
        for j in range(0, 17):
            product = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
            if product > greatest_product:
                greatest_product = product
            j += 1
        i += 1

    # Check verticals
    for i in range(0, 17):
        for j in range(0, 20):
            product = grid[i][j] * grid[i+1][j] * grid[i+2][j] * grid[i+3][j]
            if product > greatest_product:
                greatest_product = product
            j += 1
        i += 1

    # Check diagonals
    for i in range(0, 17):
        for j in range(0, 17):
            product = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
            if product > greatest_product:
                greatest_product = product
            j += 1
        i += 1

    for i in reversed(range(0, 17)):
        for j in reversed(range(0, 17)):
            product = grid[i][j+3] * grid[i+1][j+2] * grid[i+2][j+1] * grid[i+3][j]
            if product > greatest_product:
                greatest_product = product
            j -= 1
        i -= 1

    print(greatest_product)


def prepare_grid():

    # Create a list to hold lists of numbers
    grid = []

    # Read the grid from the file
    file = open("grid.txt", "rU")

    # Read each line and append numbers into the list
    for line in file:
        # Strip trailing newlines
        line = line.rstrip()

        # Split the line at whitespaces and append numbers to the list
        grid.append([int(i) for i in line.split()])

    file.close()

    return grid


if __name__ == '__main__':
    start = time.time()
    main()
    finish = time.time()
    print("TOOK " + str(finish - start) + " SECONDS")
