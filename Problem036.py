'''
Created on Jun 2, 2022

@author: Jim Yin
'''

import time

def palin(n):
    return str(n) == str(n)[::-1]

def main():
    print(sum(i for i in range(1, 10**6) if palin(i) and palin(str(bin(i))[2:])))

if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')

'''
872187
'''

'''
Time taken = 0.5549615 sec
'''