'''
Created on Jan 27, 2019

@author: Jim Yin
'''

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
            # if we get here we completed our inner loop
            # which means no i % j was equal to 0
            results += 0
    return results
            

print(sum((i for i in range(5, 2000000, 2) if isPrime(i)), 5))

'''
142913828922
'''
