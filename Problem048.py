'''
Created on May 25, 2022

@author: Jim Yin
'''


'''
The series, 1**1 + 2**2 + 3**3 + ... + 10**10 = 10405071317.

Find the last ten digits of the series, 1**1 + 2**2 + 3**3 + ... + 1000**1000.
'''

def self_power_last_digits(n):
    total = 1
    counter = 1
    while counter <= n:
        total *= n
        counter += 1
        total = total % 100000000000
    
    return total

print(sum(self_power_last_digits(i) for i in range(1, 1001)) % 10000000000)

'''
9110846700
'''
