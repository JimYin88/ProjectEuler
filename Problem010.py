# Created on Jan 27, 2019
#
# @author: Jim Yin

from sympy import isprime
import time


def prime_gen(upper_limit):
    # start at 5 and use a step of 2
    results = 5
    for i in range(5, upper_limit, 2):
        # loop from 2 to i
        if isprime(i):
            results += i
        else:
            # if we get here we completed our inner loop
            # which means no i % j was equal to 0
            results += 0
    return results
            

if __name__ == '__main__':
    start_time = time.perf_counter()
    print(sum((i for i in range(5, 2000000, 2) if isprime(i)), 5))
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 142913828922
# Time taken = 3.8082388 sec