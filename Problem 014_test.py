# Problem 14
# Which starting number, under one million, produces the longest chain of Collatz Conjecture?

import time


def main():

    collatz_list = []

    longest_chain = 0

    longest_chain_starter = 0

    i = 1

    while i < 1000000:

        num = collatz(i)

        while True:

            collatz_list.append(num)

            if num == 1:
                break
            else:
                num = collatz(num)

        if longest_chain < len(collatz_list):

            longest_chain_starter = i

            longest_chain = len(collatz_list)

        collatz_list = []

        i += 1

    print(longest_chain_starter)


def collatz(num):

    if num % 2 == 0:
        return num / 2
    else:
        return 3 * num + 1


if __name__ == '__main__':
    start = time.time()
    main()
    finish = time.time()
    print("TOOK " + str(finish - start) + " SECONDS")
