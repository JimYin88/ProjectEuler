'''
Created on May 21, 2022

@author: Jim Yin
'''

'''
2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?
'''

num = 2**1000
numstring = str(num)

total = 0
for d in numstring:
    total += int(d)

print(total)    