'''
Created on Jan 27, 2019

@author: Jim Yin
'''


def collatzcount(n):
    result = 1
    if n == 1:
        return result
    while n > 1:
        if n %2 == 0:
            n /= 2
            result += 1
        else:
            n = 3*n + 1
            result += 1
    return result

highestcollatzcount = 1
highestcollatz = 1

for i in range(1000000):
    x = collatzcount(i)
    if x > highestcollatzcount:
        highestcollatzcount = x
        highestcollatz = i
    
print(highestcollatz)

'''
837799
'''