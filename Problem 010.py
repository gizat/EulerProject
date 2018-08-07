# Problem 10
# Find the sum of all the primes below two million.

import time


def main():

    number = 1

    prime_numbers = []

    while number < 2000000:

        if is_prime(number):
            prime_numbers.append(number)

        number += 1

    print(sum_primes(prime_numbers))


def is_prime(n):
    if n <= 1:
        return False
    elif n <= 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    i = 5

    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6

    return True


def sum_primes(prime_numbers):

    sum_of_primes = 0

    for prime in prime_numbers:
        sum_of_primes += prime

    return sum_of_primes


if __name__ == '__main__':
    start = time.time()
    main()
    finish = time.time()
    print("TOOK " + str(finish - start) + " SECONDS")
