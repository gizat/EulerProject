# Problem 5
# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
#
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?


def main():

    number = 1

    found = False

    while found is False:
        for i in range(1, 21):
            if number % i == 0:
                if i == 20:
                    found = True
                else:
                    continue
            else:
                break

        if found is True:
            break

        number += 1

    print("Number is:" + str(number))


if __name__ == '__main__':
    main()
