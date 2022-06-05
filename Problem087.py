'''
Created on Jun 3, 2022

@author: Jim Yin
'''

import math
import time

time_start = time.perf_counter()

def prime_gen(lowerlimit, upperlimit):
    num = max(2, lowerlimit)
    if num == 2:
        yield num
        num += 1

    if num == 3:
        yield num
        num += 2
        
    if num % 2 == 0:
        num += 1

    while num < upperlimit:
        isprime = True
        
        for x in range(3, int(math.sqrt(num)) + 1, 2):
            if num % x == 0: 
                isprime = False
                break
        
        if isprime:
            yield num
        
        num += 2

def main():
    target = 50000000
    prime_list2 = [x for x in prime_gen(2, int(target**0.5)+1)]
    prime_list3 = [x for x in prime_gen(2, int(target**(1/3))+1)]                                    
    prime_list4 = [x for x in prime_gen(2, int(target**(1/4))+1)] 
    
    print(len(set([x**2 + y**3 + z**4 for x in prime_list2 for y in prime_list3 for z in prime_list4 if x**2 + y**3 + z**4 < target])))
    
if __name__ == '__main__':
    main()

'''
1097343
'''

time_end = time.perf_counter()
print(f'Time taken = {time_end - time_start} sec')

'''
Time taken = 2.3967444 sec
'''





