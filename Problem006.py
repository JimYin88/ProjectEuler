# Created on Jan 27, 2019
#
# @author: Jim Yin

# The sum of the squares of the first ten natural numbers is,
# 12 + 22 + ... + 102 = 385
# The square of the sum of the first ten natural numbers is,
# (1 + 2 + ... + 10)2 = 552 = 3025
# Hence the difference between the sum of the squares of the first ten natural numbers
# and the square of the sum is 3025 − 385 = 2640.
# Find the difference between the sum of the squares of the first one hundred natural numbers
# and the square of the sum.

import time


def prob_006():
    sumofsquares = sum([x*x for x in range(1, 101)])
    squareofsums = sum([x for x in range(1,101)]) * sum([x for x in range(1,101)])
    return squareofsums - sumofsquares


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_006())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 25164150
# Time taken = 3.999999999999837e-05 sec