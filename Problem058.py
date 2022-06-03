'''
Created on Jun 3, 2022

@author: Jim Yin
'''

import math
import time

time_start = time.time()


def is_prime(n):
    if n == 1:
        return False 
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0:
        return False
    else:
        for i in range(3, int(math.sqrt(n))+1, 2):
            if n%i==0:
                return False
    return True

def find_spiral_primes():
    layer = 3
    number_prime = 0
    number_nonprime = 1
    
    while True:
        lower_right = [layer**2]
        lower_left = [layer**2 - layer + 1]
        upper_left = [layer**2 - 2*layer + 2]
        upper_right = [layer**2 - 3*layer + 3]
        
        diagonal = lower_right + lower_left + upper_left + upper_right
        
        for n in diagonal:
            if is_prime(n):
                number_prime += 1
            else:
                number_nonprime += 1
        
        if number_prime/(number_prime + number_nonprime) < 0.1:
            return layer
        else:
            layer += 2
        
print(find_spiral_primes())

'''
26241
'''

time_end = time.time()
print("time taken", time_end-time_start)

'''
time taken 4.609025001525879
'''
