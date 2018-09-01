# Problem 14
# Which starting number, under one million, produces the longest chain of Collatz Conjecture?

import time
import sys

# A dictionary to store the number and it's chain size in the sequence
chain_sizes = {1: 1}

# The number that starts the longest chain in the sequence
number = -1

longest_chain = 0


def main():

    global number
    global longest_chain

    # As many values are being recalculated, there's no need to compute the chain for any number below 500,000.
    for i in range(500000, 1000000 - 1):
        if count_chain(i) > longest_chain:
            longest_chain = count_chain(i)
            number = i

    print(number)


# Count the chain size of a number and store in the dictionary
def count_chain(num):
    global chain_sizes

    # If the input number is in the list, then return it's values (chain size).
    if num in chain_sizes:
        return chain_sizes[num]

    # Perform ordinary operation if num is odd.
    if num % 2 == 0:
        chain_sizes[num] = 1 + count_chain(num / 2)

    # If num is odd, then 3 * num + 1 is even, therefore save a step by dividing by 2.
    else:
        chain_sizes[num] = 2 + count_chain((3 * num + 1) / 2)

    return chain_sizes[num]


if __name__ == '__main__':
    start = time.time()
    main()
    finish = time.time()
    print("TOOK " + str(finish - start) + " SECONDS")
