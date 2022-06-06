# Created on Jan 27, 2019
#
# @author: Jim Yin


# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?


def main():
    remainder = 600851475143
    divider = 2
    result = []
    while remainder > 1:
        if remainder % divider == 0:
            result.append(divider)
            remainder /= divider
        else:
            divider += 1

    print(max(result))


if __name__ == '__main__':
    main()


# 6857

