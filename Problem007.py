'''
Created on Jan 27, 2019

@author: Jim Yin
'''

import math
import time

time_start = time.perf_counter()

def prime_nth_term(n):
    if n == 1:
        return 2

    if n == 2:
        return 3

    target_num = 5
    primecount = 2

    while primecount < n:
        isprime = True
        
        for x in range(3, int(math.sqrt(target_num)) + 1, 2):
            if target_num % x == 0: 
                isprime = False
                break
        
        if isprime:
            primecount += 1
        if primecount == n:
            return target_num
        
        target_num += 2

print(prime_nth_term(10001))

'''
104743
'''

time_end = time.perf_counter()
print(f"time taken = {time_end-time_start} sec")

'''
time taken 0.12167109999999999 sec
'''