# Created on Jun 10, 2022
#
# @author: Jim Yin

import time
start_time = time.perf_counter()

layer = 20
path_init = {(0, 0): 1}
path_pre = path_init
path_next = []

for i in range(layer*2):
    for x, y in path_pre:
        if x+1 <= 20:
            path_next.append([(x+1, y), path_pre[(x,y)]])
        if y+1 <= 20:
            path_next.append([(x, y+1), path_pre[(x,y)]])

    path_next_dict = {}

    for j in path_next:
        if j[0] not in path_next_dict:
            path_next_dict[j[0]] = j[1]
        else:
            path_next_dict[j[0]] += j[1]

    path_pre = path_next_dict
    path_next = []

print(path_pre[(20, 20)])
end_time = time.perf_counter()
print(f'Time taken = {end_time - start_time} sec')


# 137846528820
# Time taken = 0.0008680000000000077 sec
