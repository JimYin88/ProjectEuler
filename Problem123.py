'''
Created on May 26, 2022

@author: Jim Yin
'''

'''
Let pn be the nth prime: 2, 3, 5, 7, 11, ..., and let r be the remainder when (pn−1)**n + (pn+1)**n is divided by pn**2.

For example, when n = 3, p3 = 5, and 43 + 63 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 10**9 is 7037.

Find the least value of n for which the remainder first exceeds 10**10.
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
        
for n, pn in enumerate(prime_gen()):
    if ((2*(n+1)*pn)%(pn*pn) > math.pow(10,10) and n%2 == 0):
        print(n+1)
        break

'''
21035
'''