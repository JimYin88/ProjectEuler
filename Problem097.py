'''
Created on May 31, 2022

@author: Jim Yin
'''

def last_ten_digits_power2(n):
    num = 1
    p = 0
    while p < n:
        num *= 2
        num = num % 10**10
        p += 1
      
    return num  
    
print((28433*last_ten_digits_power2(7830457)+1)%10**10)

'''
8739992577
'''