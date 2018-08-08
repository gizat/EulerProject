# Problem 13
# Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

import time


def main():

    sum_numbers = 0

    first_ten = ""

    # Read the numbers from the file
    file = open("prob13_numbers.txt", "rU")

    # Read each line and append numbers into the list
    for line in file:
        # Strip trailing newlines
        line = line.rstrip()

        sum_numbers += int(line)

    file.close()

    for digit in range(0, 10):
        first_ten += str(sum_numbers)[digit]

    print(first_ten)


if __name__ == '__main__':
    start = time.time()
    main()
    finish = time.time()
    print("TOOK " + str(finish - start) + " SECONDS")
