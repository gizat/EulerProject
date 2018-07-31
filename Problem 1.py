# Problem 1
# If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
# The sum of these multiples is 23.
#
# Find the sum of all the multiples of 3 or 5 below 1000.


# Main function
def main():
    # Counter
    i = 1

    # Sum of multiples of 3 and 5
    multiples_sum = 0

    # Iterate through each number until 1000 to find the multiples of 3 and 5
    while i < 1000:
        if i % 3 == 0 or i % 5 == 0:
            multiples_sum += i
            print(i)
        i += 1

    print("SUM IS: " + str(multiples_sum))


if __name__ == '__main__':
    main()