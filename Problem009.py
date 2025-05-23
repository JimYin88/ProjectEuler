# Created on Jan 27, 2019
#
# @author: Jim Yin


# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
# a**2 + b**2 = c**2
# For example, 3**2 + 4**2 = 9 + 16 = 25 = 5**2.
# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

import time


def prob_009():
    for i in range(1, 500):
        for j in range(i, 500):
            k = (i*i + j*j)**0.5
            if i + j + k == 1000:
                return int(i*j*k)
        

if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_009())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 31875000
# Time taken = 0.021523000003071502 sec
