# Problem 12
# What is the value of the first triangle number to have over five hundred divisors?

import math
import time


def main():

    i = 1

    triangle_number = 0

    while True:
        # Find the next triangle number
        triangle_number += i

        if find_divisors(triangle_number) > 500:
            print(triangle_number)
            return False

        i += 1


def find_divisors(num):

    num_divisors = 0

    i = 1

    # Loop till square root
    while i <= math.sqrt(num):

        if num % i == 0:
            # Use only one divisor, if they're equal
            if num / i == i:
                num_divisors += 1
            # Append two divisors into the list
            else:
                num_divisors += 2

        i += 1

    return num_divisors


if __name__ == '__main__':
    start = time.time()
    main()
    finish = time.time()
    print("TOOK " + str(finish - start) + " SECONDS")
