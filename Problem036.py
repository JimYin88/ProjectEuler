'''
Created on Jun 2, 2022

@author: Jim Yin
'''

def palin(n):
    return str(n) == str(n)[::-1]

print(sum(i for i in range(1, 10**6) if palin(i) and palin(str(bin(i))[2:])))

'''
872187
'''
