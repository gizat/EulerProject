# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


def main():

    prime_counter = 0

    number = 2

    while True:

        is_prime = True

        for i in range(2, number):
            if number % i == 0:
                is_prime = False
                break

        if is_prime:
            prime_counter += 1

        if prime_counter == 10001:
            print(number)
            return False

        number += 1


if __name__ == '__main__':
    main()
