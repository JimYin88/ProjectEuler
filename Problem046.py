'''
Created on Feb 2, 2019

@author: JimYi
'''

def isprime(n):
    """check if integer n is a prime"""
    # range starts with 2 and only needs to go up the squareroot of n
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True


def goldbach_gen(n):
    goldbach_num = 1
    while goldbach_num <= n:
        goldbach_num += 2
        if isprime(goldbach_num) == False:
            yield goldbach_num
        
y = goldbach_gen(100)
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))
print(next(y))

print(isprime(99))



