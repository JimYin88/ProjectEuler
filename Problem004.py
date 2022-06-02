'''
Created on Jan 27, 2019

@author: Jim Yin
'''

def palin(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    print(max(x * y for x in range(100,1000) for y in range(100,1000) if palin(x*y)))

'''
906609
'''    