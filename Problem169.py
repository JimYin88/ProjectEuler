'''
Created on May 31, 2022

@author: Jim Yin
'''

'''
Define f(0)=1 and f(n) to be the number of different ways n can be expressed as a sum of integer powers of 2 using each power no more than twice.

For example, f(10)=5 since there are five different ways to express 10:

1 + 1 + 8
1 + 1 + 4 + 4
1 + 1 + 2 + 2 + 4
2 + 4 + 4
2 + 8

What is f(10**25)?
'''

import math

def sum_power_2(num):
    pow_2 = int(math.log2(num))
    list_o = {num: 1}

    while pow_2 >= 0:
    
        list_n = [[rem1 - (2**pow_2)*j, list_o[rem1]] for rem1 in list_o for j in range(3)]
        
        list_n_filter = [[rem2, t2] for rem2, t2 in list_n if (rem2 <= (2**(pow_2-1))*4-2 and rem2 >= 0)]
        list_n = list_n_filter
        
        list_n_dict = dict()
        for rem3, t3 in list_n_filter:
            if rem3 not in list_n_dict:
                list_n_dict[rem3] = t3
            else:
                list_n_dict[rem3] += t3
        
        list_o = list_n_dict
        
        pow_2 -= 1

    return list_o[0]

print(sum_power_2(10**25))


'''
178653872807
'''
