'''
Created on Jan 27, 2019

@author: JimYi
'''

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
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
            
x = prime_gen(2000000)

print(x)

'''
142913828922
'''
