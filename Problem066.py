'''
Created on Jan 28, 2019

@author: Jim Yin
'''

'''
Consider quadratic Diophantine equations of the form:
x2 - Dy2 = 1
For example, when D=13, the minimal solution in x is 6492 – 13×1802 = 1.
It can be assumed that there are no solutions in positive integers when D is square.
By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:
32 – 2×22 = 1
22 – 3×12 = 1
92 – 5×42 = 1
52 – 6×22 = 1
82 – 7×32 = 1
Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.
Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
'''


d = (x for x in range(2, 1001) if x not in [y*y for y in range(2,40)])

def diophantinesolver(d):
    x = 2
    y = int(((x**2 - 1)/d)**0.5)
    while x**2 - d * y**2 != 1:
        x += 1
        y = int(((x**2 - 1)/d)**0.5)
    return x


highestd = 2
highestx = 3

for i in d:
    x = diophantinesolver(i)
    if x > highestx:
        highestx = x
        highestd = i
    
print(highestx, highestd)


