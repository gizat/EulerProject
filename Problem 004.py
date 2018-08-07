# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from
# the product of two 2-digit numbers is 9009 = 91 × 99.
#
# Find the largest palindrome made from the product of two 3-digit numbers.


def main():

    # The product of the largest 3-digit numbers 999 and 999
    number = 999*999

    while True:
        if is_palindrome(number):
            for i in range(999, 100, -1):
                if number % i == 0:
                    if len(str(int(number / i))) == 3:
                        print("The largest palindrome made from the product of two 3-digit numbers is: " + str(number))
                        print("num1: " + str(i))
                        print("num2: " + str(int(number / i)))
                        return False

        number -= 1


# Check for a palindrome
def is_palindrome(number):

    i = 0

    # Change to a convenient type
    number = str(number)

    # Do operations till the first mismatch or the half of the length of the number
    while i < len(number)/2:
        if number[i] == number[(len(number) - 1) - i]:
            i += 1
        else:
            return False

    return True


if __name__ == '__main__':
    main()
