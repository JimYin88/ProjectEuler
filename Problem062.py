'''
Created on Jun 3, 2022

@author: Jim Yin
'''

import time
time_start = time.perf_counter()

def find_permutation(max_x):
    perm_storage = {}
    x = 1
    while x <= max_x:
        perm_storage[x] = ''.join(sorted(str(x**3)))
        x += 1
            
    return perm_storage
        
p = find_permutation(10000)

for i in p:
    if sum(1 for j in p if p[i] == p[j]) == 5:
        print(i**3)
        break  

'''
127035954683
'''

time_end = time.perf_counter()
print(f"time taken = {time_end - time_start} sec")

'''
time taken = 7.3882631 sec
'''  
