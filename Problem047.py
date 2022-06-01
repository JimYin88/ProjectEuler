'''
Created on May 31, 2022

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

def n_dist_prime_factors(num):
    d = []
    n = num
    while n > 1:
        for p in prime_list:
            if n % p == 0:
                while n % p == 0:
                    n /= p 
                d.append(p)
    return d

def distinct_primes_factors():
    
    list01 = [[i+2, n_dist_prime_factors(i+2)] for i in range(4)]
    num1, p_factors1 = list01[0][0], list01[0][1]
    num2, p_factors2 = list01[1][0], list01[1][1]
    num3, p_factors3 = list01[2][0], list01[2][1]
    num4, p_factors4 = list01[3][0], list01[3][1]
    
    num_next = 6
    
    while True:
        if len(p_factors1) == len(p_factors2) == len(p_factors3) == len(p_factors4) == 4:
            if set(p_factors1).intersection(p_factors2) == set():
                if set(p_factors2).intersection(p_factors3) == set():
                    if set(p_factors3).intersection(p_factors4) == set():
                        return num1
        else:
            num1, p_factors1 = num2, p_factors2
            num2, p_factors2 = num3, p_factors3
            num3, p_factors3 = num4, p_factors4
            num4, p_factors4 = num_next, n_dist_prime_factors(num_next)
            num_next += 1
            
print(distinct_primes_factors())

'''
134043
'''



    