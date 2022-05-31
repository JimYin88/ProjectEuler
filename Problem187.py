'''
Created on May 28, 2022

@author: JimYi
'''

'''
How many composite integers, n < 10**8, have precisely two, not necessarily distinct, prime factors?
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
        
        for x in range(3, int(math.sqrt(num) + 1), 2):
            if num % x == 0: 
                isprime = False
                break
        
        if isprime:
            yield num
        
        num += 2

def composite_count(n):
    primelist = [p for p in prime_gen(1, int(math.sqrt(n)+1))]
    total = int(len(primelist)*(len(primelist)+1)/2)
    for q in prime_gen(primelist[-1]+1, int(n/2)+1):
        for r in primelist:
            if q*r <= n:
                total += 1
            else:
                break
            
    return total              

print(composite_count(100000000))

'''
17427258
'''
        