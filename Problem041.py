# Created on Jun 16, 2022
#
# @author: Jim Yin

import time 


def isPrime(n):
    if n == 1 or n == 4:
        return False 
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n%i==0:
                return False
    return True


def prime_gen(upper_limit):
    # start at 5 and use a step of 2
    results = 5
    for i in range(5, upper_limit, 2):
        # loop from 2 to i
        if isPrime(i):
            results += i
        else:
            results += 0
    return results
            

def pandigital_prime(n):
    if '0' in str(n):
        return False
    return set(str(n)) == {str(i) for i in range(1, len(str(n))+1)}
               

def prob_041():
    prime_list = [i for i in range(1_000_001, 10_000_000, 2) if isPrime(i)]
    # Need to check only 7 digits prime since 8 and 9-digits pandigitals are
    # divisible by 3.

    for i in (prime_list[::-1]):
        if pandigital_prime(i):
            print(i)
            break
    
if __name__ == '__main__':
    start_time = time.perf_counter()
    prob_041()
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')
    

# 7652413
# Time taken = 71.41677490000001 sec
