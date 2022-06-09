'''
Created on May 26, 2022

@author: Jim Yin
'''

'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''

import math

def prime_gen():
    yield 2
    yield 3
    num = 5
    
    while True:
        isprime = True
        
        for x in range(3, int(math.sqrt(num) + 1), 2):
            if num % x == 0: 
                isprime = False
                break
        
        if isprime:
            yield num
        
        num += 2

def is_prime(num):
    if num == 1:
        return False
    if num == 2:
        return True
    if num == 3:
        return True
    if num % 2 == 0:
        return False
        
    for x in range(3, int(math.sqrt(num) + 1), 2):
        if num % x == 0:
            return False
        else:
            continue
        
    return True   
        
def trunctable(num):
    if len(str(num)) == 1:
        return False

    for t in range(len(str(num))-1):
        if not is_prime(int(str(num)[t+1:])):
            return False 
    
    for t in range(len(str(num))-1):
        if not is_prime(int(str(num)[0:-(t+1)])):
            return False 
    
    return True

print(sum([i for i in range(1000000) if is_prime(i) and trunctable(i)]))

'''
748317
'''        
            