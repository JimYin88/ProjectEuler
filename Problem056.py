'''
Created on May 24, 2022

@author: Jim Yin
'''

'''
A googol (10**100) is a massive number: one followed by one-hundred zeros; 100**100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''

def sum_of_digit(n):
    total = 0
    for d in str(n):
        total += int(d)
    return total

power_gen = (i**j for i in range(1, 100) for j in range(1, 100))

max_total = 0
for p in power_gen:
    if sum_of_digit(p) > max_total:
        max_total = sum_of_digit(p)

print(max_total)

'''
972
'''