# Problem 10
# Find the sum of all the primes below two million.


def main():

    number = 7

    prime_numbers = [2, 3, 5]

    sum_of_primes = 0

    while number < 2000000:

        is_prime = True

        if number % 2 == 0 or sum_digits(number) % 3 == 0 or number % 5 == 0:
            is_prime = False
        else:
            for prime in prime_numbers:
                if number % prime == 0:
                    is_prime = False

        if is_prime:
            prime_numbers.append(number)
            print("----------")
            print(number)

        number += 1

    for prime in prime_numbers:
        sum_of_primes += prime

    print(sum_of_primes)


def sum_digits(num):
    r = 0

    while num:
        r, num = r + num % 10, num // 10

    return r


if __name__ == '__main__':
    main()
