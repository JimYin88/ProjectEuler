# Created on Jan 27, 2019
#
# @author: Jim Yin



# 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20

import time


def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


def prob_005():
    result = 1
    for x in range(1,21):
        result = lcm(result, x)
    print(result)
    

if __name__ == '__main__':
    start_time = time.perf_counter()
    prob_005()
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')
    
    
# 232792560
# Time taken = 4.0399999999995995e-05 sec

   

    