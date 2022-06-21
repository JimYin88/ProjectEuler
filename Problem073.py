# Created on Jun 20, 2022
#
# @author: JimYi

import time
import math
from tqdm import tqdm


def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a


def prob_073(upperlimit):
    result = 0
    for d in tqdm(range(4, upperlimit)):
        for n in range(math.floor(d/3), math.ceil(d/2)+1):
            if n/d <= 1/3:
                n += 1
            elif n/d >= 1/2:
                break
            elif gcd(n, d) > 1:
                n += 1
            else:
                result += 1
                n += 1
            
    return result


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_073(12001))
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')
    

# 7295372
# Time taken = 12.8598452 sec
