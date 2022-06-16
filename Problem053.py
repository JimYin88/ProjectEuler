# Created on May 26, 2022
#
# @author: Jim Yin


# How many, not necessarily distinct, values of (n r) for 1 <= n <= 100 are greater than one-million?


import math
import time


def prob_053():
    print(sum(1 for n in range(1, 101) for r in range(1, n) if math.comb(n, r) > 1000000))


if __name__ == '__main__':
    start_time = time.perf_counter()
    prob_053()
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 4075
# Time taken = 0.007283099999999987 sec