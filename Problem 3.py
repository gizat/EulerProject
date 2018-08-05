# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.

# What is the largest prime factor of the number 600851475143?


def main(number):

    # Hold prime factors
    prime_factors = []

    # Initial counter, first prime number
    i = 2

    # Find primes of the number
    while number > 1:

        # Find primes
        if number % i == 0:
            prime_factors.append(i)

            # Set the number to self divided by the prime
            number /= i
        else:
            i += 1

    for number in prime_factors:
        print(number)


if __name__ == '__main__':
    main(600851475143)