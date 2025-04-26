# Created on April 10, 2025
#
# @author: Jim Yin


import time
from itertools import permutations


def prob_024():

    perm = permutations(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    count = 1
    num = next(perm)

    while count < 10**6:
        num = next(perm)
        count += 1

    return int(''.join(list(num)))


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_024())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 2783915460
# Time taken = 0.19971630000145524 sec
