# Problem 7
# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
# What is the 10 001st prime number?


def main():

    number = 7

    prime_numbers = [2, 3, 5]

    while len(prime_numbers) < 10001:

        is_prime = True

        if number % 2 == 0 or sum_digits(number) % 3 == 0 or number % 5 == 0:
            is_prime = False
        else:
            for prime in prime_numbers:
                if number % prime == 0:
                    is_prime = False

        if is_prime:
            prime_numbers.append(number)

        number += 1

    print(prime_numbers[10000])


def sum_digits(num):
    r = 0

    while num:
        r, num = r + num % 10, num // 10

    return r


if __name__ == '__main__':
    main()
