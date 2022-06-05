'''
Created on Jun 2, 2022

@author: Jim Yin
'''

from functools import cache

import time
time_start = time.time()

@cache
def find_coin_partition(target, maxcoin, multiplier):
    if maxcoin == 0:
        return 0
    val_prev = {target: 1}
    
    for i in range(maxcoin, maxcoin-1, -1):
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
    
    return sum([find_coin_partition(k, maxcoin - 1, multiplier * v) if k >= 1 else v for k, v in val_prev.items()])

def main():
    i = 10
    while True:            
        if find_coin_partition(i, i, 1) % 10**3 == 0:
            return i 
        else:
            i += 1

print(main())

# def find_coin_partition(target):
#     val_prev = {target: 1}
#
#     for i in range(target, 0, -1):
#         val_next = {}
#         for val in val_prev:
#             num_of_subtraction = 0
#             while val - num_of_subtraction*i >= 0:
#                 if (val - num_of_subtraction*i) not in val_next:
#                     val_next[val - num_of_subtraction*i] = val_prev[val]
#                 else:
#                     val_next[val - num_of_subtraction*i] += val_prev[val]
#
#                 num_of_subtraction += 1
#
#         val_consolidate = {}
#         for k in val_next:
#             if k not in val_consolidate:
#                 val_consolidate[k] = val_next[k]
#             else:
#                 val_consolidate[k] += val_next[k]
#
#         val_prev = val_consolidate
#
#     return val_prev[0], val_prev
#
# def main():
#     i = 10
#     while True:            
#         if find_coin_partition(i) % 10**4 == 0:
#             return i 
#         else:
#             i += 1

# print(main())

# print(find_coin_partition(4))

#
#
# def find_coin_partition(num_ways):
#     target = 2
#     while True:
#         val_initial = {target: 1}
#         val_prev = val_initial
#
#         for i in range(target, 0, -1):
#             val_next = {}
#             for val in val_prev:
#                 num_of_subtraction = 0
#                 while val - num_of_subtraction*i >= 0:
#                     if (val - num_of_subtraction*i) not in val_next:
#                         val_next[val - num_of_subtraction*i] = val_prev[val]
#                     else:
#                         val_next[val - num_of_subtraction*i] += val_prev[val]
#
#                     num_of_subtraction += 1
#
#             val_consolidate = {}
#             for k in val_next:
#                 if k not in val_consolidate:
#                     val_consolidate[k] = val_next[k]
#                 else:
#                     val_consolidate[k] += val_next[k]
#
#             val_prev = val_consolidate
#
#         if 0 not in val_prev:
#             target += 1
#         elif val_prev[0] < num_ways:
#             target += 1
#         else:
#             return target
#
# print(find_coin_partition(10**6))


#
#
# coin_start = 5
# rem_initial = {coin_start: 1}
# rem_prev = rem_initial
#
# for i in range(coin_start, 0, -1):
#     rem_next = {}
#     for rem in rem_prev:
#         num_of_subtraction = 0
#         while rem - num_of_subtraction*i >= 0:
#             if (rem - num_of_subtraction*i) not in rem_next:
#                 rem_next[rem - num_of_subtraction*i] = rem_prev[rem]
#             else:
#                 rem_next[rem - num_of_subtraction*i] += rem_prev[rem]
#
#             num_of_subtraction += 1
#
#     rem_consolidate = {}
#     for k in rem_next:
#         if k not in rem_consolidate:
#             rem_consolidate[k] = rem_next[k]
#         else:
#             rem_consolidate[k] += rem_next[k]
#
#     rem_prev = rem_consolidate
#
# print(rem_prev[0])            
                
'''
190569291
'''

time_end = time.time()
print("time taken", time_end-time_start)

'''
time taken 0.01896977424621582
'''
        