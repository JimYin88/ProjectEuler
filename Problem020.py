'''
Created on May 25, 2022

@author: Jim Yin
'''

'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

import math
import time


def count_digit(n):
    return sum(int(d) for d in str(n))


def main():
    start_time = time.perf_counter()
    print(count_digit(math.factorial(100)))
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


if __name__ == '__main__':
    main()


# 648
# Time taken = 6.310000000000343e-05 sec
