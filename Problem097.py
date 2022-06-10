# Created on May 31, 2022
#
# @author: Jim Yin

import time


def last_ten_digits_power2(n):
    """
    :param n: the nth power of 2
    :return: the last 10 digit of 2**n
    """
    num = 1
    p = 0
    while p < n:
        num *= 2
        num = num % 10**10
        p += 1
      
    return num  


def prob_097():
    print((28433*last_ten_digits_power2(7830457)+1)%10**10)


if __name__ == '__main__':
    start_time = time.perf_counter()
    prob_097()
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 8739992577
# Time taken = 2.0336144000000003 sec
