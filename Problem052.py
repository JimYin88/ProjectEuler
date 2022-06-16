'''
Created on Jun 2, 2022

@author: Jim Yin
'''

'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''

def permuted_multiples():
    n = 10000
    while True:
        if (len(str(n)) == len(str(6*n))) and set(str(n)) == set(str(2*n)) and set(str(n)) == set(str(3*n)) and set(str(n)) == set(str(4*n)) \
        and set(str(n)) == set(str(5*n)) and set(str(n)) == set(str(6*n)):
            return n 
        else:
            n += 1
            
print(permuted_multiples())

'''
142857
'''
