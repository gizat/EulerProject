# Problem 9
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.


def main():

    for a in range(1, 1001):
        for b in range(a+1, 1001):
            for c in range(b+1, 1001):

                if a**2 + b**2 == c**2:
                    if a + b + c == 1000:
                        print(a*b*c)


if __name__ == '__main__':
    main()
