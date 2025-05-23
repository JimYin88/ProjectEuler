# Created on Jun 2, 2022
#
# @author: Jim Yin


import math
import time


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


prime_list = [x for x in prime_gen(2, 10**4)]


def prob_077(num_ways):
    target = 10
    while True:
        val_initial = {target: 1}
        val_prev = val_initial
        prime_target = [x for x in prime_list if x < target]
        prime_target.reverse()
        
        for i in prime_target:
            val_next = {}
            for val in val_prev:
                num_of_subtraction = 0
                while val - num_of_subtraction*i >= 0:
                    if (val - num_of_subtraction*i) not in val_next:
                        val_next[val - num_of_subtraction*i] = val_prev[val]
                    else:
                        val_next[val - num_of_subtraction*i] += val_prev[val]
        
                    num_of_subtraction += 1
        
            val_consolidate = {}
            for k in val_next:
                if k not in val_consolidate:
                    val_consolidate[k] = val_next[k]
                else:
                    val_consolidate[k] += val_next[k]
        
            val_prev = val_consolidate
        
        if 0 not in val_prev:
            target += 1
        elif val_prev[0] <= num_ways:
            target += 1
        else:
            return target


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_077(num_ways=5000))
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 71
# Time taken = 0.019228700009989552 sec
