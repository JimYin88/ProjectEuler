'''
Created on May 25, 2022

@author: JimYi
'''

'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        
    return result


def digit_factorials(n):
    return n == sum(factorial(int(i)) for i in str(n))

print(sum(i for i in range(3, factorial(10)) if digit_factorials(i)))

'''
40730
'''
