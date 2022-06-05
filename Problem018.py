'''
Created on May 26, 2022

@author: Jim Yin
'''

import time

time_start = time.perf_counter()

s = [[75],
     [95, 64],
     [17, 47, 82],
     [18, 35, 87, 10],
     [20, 4, 82, 47, 65],
     [19, 1, 23, 75, 3, 34],
     [88, 2, 77, 73, 7, 63, 67],
     [99, 65, 4, 28, 6, 16, 70, 92],
     [41, 41, 26, 56, 83, 40, 80, 70, 33],
     [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
     [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
     [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
     [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
     [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
     [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]]

path_pre = [75]

for i in range(2, 16):
    path_next = []
    for j in range(0, i):
        if j == 0:
            path_next.append(int(s[i-1][j])+int(path_pre[j]))
        elif j == i-1:
            path_next.append(int(s[i-1][j])+int(path_pre[j-1]))
        else:
            path_next.append(max(int(s[i-1][j])+int(path_pre[j]), int(s[i-1][j])+int(path_pre[j-1])))
            
    path_pre = path_next

print(max(path_pre))


'''
1074
'''

time_end = time.perf_counter()
print("time taken", time_end-time_start)

'''
time taken 0.00023439999999999572
'''