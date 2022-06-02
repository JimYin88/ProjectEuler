'''
Created on Jun 1, 2022

@author: Jim Yin
'''

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

prime_list = [x for x in prime_gen(2, 10**6)]



def circularprime(n):
    for i in range(len(str(n))):
        if int(str(n)[i:]+str(n)[0:i]) not in prime_list:
            return False
    return True 

print(sum(1 for x in prime_list if circularprime(x)))

'''
55
'''
