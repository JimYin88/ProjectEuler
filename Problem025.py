'''
Created on Jan 27, 2019

@author: JimYi
'''


def fibbonacci_gen(n):
    counter = 0
    a = 0
    b = 1
    while counter < n:
        a, b = b, a+b
        counter += 1
        yield a

def number_of_digit(n):
    return len(str(n))


def fibbonacci_first(n):
    counter01 = 0     
    for x in fibbonacci_gen(100000):
        counter01 += 1
        if number_of_digit(x) == n:
            return counter01

print(fibbonacci_first(1000))
    
''' 
4782
'''   