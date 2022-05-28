'''
Created on May 28, 2022

@author: Jim Yin
'''

def hollow_square(n):
    total = 0
    for x in range(3, int(n/4+2)):
        for y in range(x-1, 0, -1):
            if x**2 - y**2 > n:
                break
            if x-y >= 2 and (x-y)%2==0:
                total += 1
    return total

print(hollow_square(1000000))

'''
1572729
'''