# Created on Feb 2, 2019
#
# @author: Jim Yin

import time
from fractions import Fraction


def prob_071():

    max_result = 0
    proper_fractions = set()
    for d in range(3, 1000000):
        for n in range(int(d * 3 / 7) - 1, int(d * 3 / 7)):
            candidate = Fraction(n, d)
            if candidate < Fraction(3, 7):
                if candidate > max_result:
                    max_result = candidate

    return max_result.numerator


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_071())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 428570
# Time taken = 4.25824600001215 sec
