'''
Created on Jun 2, 2022

@author: Jim Yin
'''

import time
time_start = time.perf_counter()

lines = []
with open("p067_triangle.txt") as f:
    for line in f.read().strip().split('\n'):
        lines.append(list(map(int, line.split(" "))))

path_pre = lines[0]

for i in range(2, 101):
    path_next = []
    for j in range(0, i):
        if j == 0:
            path_next.append(int(lines[i-1][j])+int(path_pre[j]))
        elif j == i-1:
            path_next.append(int(lines[i-1][j])+int(path_pre[j-1]))
        else:
            path_next.append(max(int(lines[i-1][j])+int(path_pre[j]), \
                                 int(lines[i-1][j])+int(path_pre[j-1])))
            
    path_pre = path_next

print(max(path_pre))

'''
7273
'''

time_end = time.perf_counter()
print(f'time taken = {time_end - time_start} sec')


'''
time taken = 0.0089331 sec
'''