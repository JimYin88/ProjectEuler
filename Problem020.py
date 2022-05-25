'''
Created on May 25, 2022

@author: Jim Yin
'''

'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
        
    return result

# print(factorial(10))

def count_digit(n):
    s = str(n)
    total = 0
    for i in s:
        total += int(i)
    
    return total

print(count_digit(factorial(100)))

'''
648
'''