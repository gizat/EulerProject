# Problem 14
# Which starting number, under one million, produces the longest chain of Collatz Conjecture?

import time


all_trees = []


def main():
    global all_trees

    for i in range(1, 10):
        one_list = []
        find_sequence(i)


def find_sequence(num):

    if num == 1:
        # Append to list here
        return 1
    elif num % 2 == 0:
        # Append to list here
        return find_sequence(num / 2)
    else:
        # Append to list here
        return find_sequence(3 * num + 1)


def test():

    dict = {1: [2, 67, 7], 2: [23, 98, 83, 3], 3: [29, 92, 83, 84, 5]}

    print(dict[3])

    print(dict)


if __name__ == '__main__':
    start = time.time()
    test()
    finish = time.time()
    print("TOOK " + str(finish - start) + " SECONDS")
