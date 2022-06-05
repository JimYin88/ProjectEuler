'''
Created on May 24, 2022

@author: Jim Yin
'''

'''
A googol (10**100) is a massive number: one followed by one-hundred zeros; 100**100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''

import time
start_time = time.perf_counter()

def sum_of_digit(n):
    total = 0
    for d in str(n):
        total += int(d)
    return total

def main():
    print(max(sum_of_digit(i**j) for i in range(1, 100) for j in range(1, 100)))

if __name__ == '__main__':
    main()

'''
972
'''
    
end_time = time.perf_counter()
print(f'Time taken = {end_time - start_time} sec')

'''
Time taken = 0.1350077 sec
'''