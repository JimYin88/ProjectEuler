'''
Created on Jun 2, 2022

@author: Jim Yin
'''

import time
time_start = time.time()

rem_initial = {100: 1}
rem_prev = rem_initial

for i in range(99, 0, -1):
    rem_next = {}
    for rem in rem_prev:
        num_of_subtraction = 0
        while rem - num_of_subtraction*i >= 0:
            if (rem - num_of_subtraction*i) not in rem_next:
                rem_next[rem - num_of_subtraction*i] = rem_prev[rem]
            else:
                rem_next[rem - num_of_subtraction*i] += rem_prev[rem]
            
            num_of_subtraction += 1
            
    rem_consolidate = {}
    for k in rem_next:
        if k not in rem_consolidate:
            rem_consolidate[k] = rem_next[k]
        else:
            rem_consolidate[k] += rem_next[k]
            
    rem_prev = rem_consolidate
         
print(rem_prev[0])            
                
'''
190569291
'''

time_end = time.time()
print("time taken", time_end-time_start)

'''
time taken 0.01896977424621582
'''
        