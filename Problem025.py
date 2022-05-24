'''
Created on Jan 27, 2019

@author: Jim Yin
'''


def fibbonacci_gen():
    a = 0
    b = 1
    while True:
        a, b = b, a+b
        yield a

def number_of_digit(n):
    return len(str(n))

def fibbonacci_first(ndigit):
    counter01 = 0     
    for x in fibbonacci_gen():
        counter01 += 1
        if number_of_digit(x) >= ndigit:
            print(counter01)
            break

fibbonacci_first(1000)
    
''' 
4782
'''   