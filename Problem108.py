'''
Created on Jun 1, 2022

@author: Jim Yin
'''

def reciprocal():
    n = 1000
    while True:
        total = 0
        for x in range(n + 1, 2*n + 1):
            if n*x % (x-n) == 0:
                total += 1
        
        if total > 1000:
            return n
        
        n += 10               
    
print(reciprocal())

'''
180180
'''