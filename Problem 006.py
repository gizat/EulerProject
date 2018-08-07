# Problem 6
# Find the difference between the sum of the squares of the first
# one hundred natural numbers and the square of the sum.


def main():

    sum_of_squares = 0
    square_of_sums = 0

    for i in range(1, 101):
        sum_of_squares += i**2
        square_of_sums += i

    square_of_sums = square_of_sums**2

    print(square_of_sums - sum_of_squares)


if __name__ == '__main__':
    main()
