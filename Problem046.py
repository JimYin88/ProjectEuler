# Created on Feb 2, 2019
#
# @author: Jim Yin

import time
import math


def prime_gen(lowerlimit, upperlimit):
    num = max(2, lowerlimit)
    if num == 2:
        yield num
        num += 1

    if num == 3:
        yield num
        num += 2
        
    if num % 2 == 0:
        num += 1

    while num < upperlimit:
        isprime = True
        
        for x in range(3, int(math.sqrt(num)) + 1, 2):
            if num % x == 0: 
                isprime = False
                break
        
        if isprime:
            yield num
        
        num += 2


prime_list = [x for x in prime_gen(2, 10**5)]


def odd_composite(num):
    if num in prime_list:
        return False
    for p in prime_list:
        if p > num:
            return True
        for i in range(1, int(math.sqrt(num/2)+1)):
            if p + 2*i**2 == num:
                return False


def find_smallest_odd_composite():
    num = 7
    while True:
        if odd_composite(num):
            return num
        else:
            num += 2


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(find_smallest_odd_composite())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 5777
# Time taken = 1.9498045000000002 sec

