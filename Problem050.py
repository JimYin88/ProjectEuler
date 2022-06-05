'''
Created on May 31, 2022

@author: Jim Yin
'''

import math
import time
time_start = time.perf_counter()

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

prime_list = [x for x in prime_gen(2, 10**6)]

max_length = 1
max_prime = 0
prime_list_length = len(prime_list)

for i in range(len(prime_list)):
    if i + max_length > prime_list_length:
        break 
    for j in range(i+max_length, len(prime_list)):
        if sum(prime_list[i:j]) > 10**6:
            break
        if sum(prime_list[i:j]) in prime_list:
            max_length = j - i 
            max_prime = sum(prime_list[i:j])
            
print(max_prime)

'''
997651
'''

time_end = time.perf_counter()
print(f'time taken = {time_end - time_start} sec')

'''
time taken = 3.6460005 sec
'''
