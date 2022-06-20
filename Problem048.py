# Created on May 25, 2022
#
# @author: Jim Yin


# The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.
#
# Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.

import time


def self_power_last_digits(n):
    total = 1
    counter = 1
    while counter <= n:
        total *= n
        counter += 1
        total = total % 100000000000
    
    return total


def prob_048():
    print(sum(self_power_last_digits(i) for i in range(1, 1001)) % 10000000000)


if __name__ == '__main__':
    start_time = time.perf_counter()
    prob_048()
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 9110846700
# Time taken = 0.1376135 sec

