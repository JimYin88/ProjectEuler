# Created on Jan 27, 2019
#
# @author: Jim Yin

# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?

import time


def prob_003(n):
    """
    Return the highest prime divider of n
    :param n: number
    :return: highest prime divider
    """
    remainder = n
    divider = 2
    result = []
    while remainder > 1:
        if remainder % divider == 0:
            result.append(divider)
            remainder /= divider
        else:
            if divider == 2:
                divider += 1
            else:
                divider += 2

    return max(result)


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_003(600851475143))
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 6857
# Time taken = 0.0008483999999999992 sec

