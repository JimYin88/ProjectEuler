'''
Created on Jan 27, 2019

@author: JimYi
'''


'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''

def triplet():
    for i in range(1,500):
        for j in range(i,500):
            k = (i*i + j*j)**0.5
            if i + j + k == 1000:
                return i*j*k
        

x = triplet()
print(x)


'''
31875000
'''