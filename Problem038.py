'''
Created on Jun 3, 2022

@author: Jim Yin

'''

import time

time_start = time.time()

def nine_digit_gen(n):
    ndigit = 0
    multiplier = 1
    n_string = ''
    while ndigit < 9:
        n_string += str(n * multiplier)
        ndigit = len(n_string)
        multiplier += 1
    if ndigit > 9:
        return 0
    elif ''.join(sorted(n_string)) == '123456789':
        return int(n_string)
    else:
        return 0

print(max(nine_digit_gen(i) for i in range(10000)))

'''
932718654
'''

time_end = time.time()
print("time taken", time_end-time_start)

'''
time taken 0.01800370216369629
'''
