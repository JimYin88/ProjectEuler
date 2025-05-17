# Created on December 18, 2014
#
# @author: Jim Yin

import time


def fib_gen():
    """
    Generates a sequence of fibonacci numbers
    """
    a = 0
    b = 1
    while True:
        a, b = b, a+b
        yield a


def number_of_digit(n):
    return len(str(n))


def prob_025(n):
    """
    Find the first fibonacci number with n digits
    """
    counter01 = 1     
    for x in fib_gen():
        if number_of_digit(x) >= n:
            return counter01
        else:
            counter01 += 1


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_025(n=1000))
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 4782
# Time taken = 0.02844080002978444 sec
