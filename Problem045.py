'''
Created on Jun 2, 2022

@author: Jim Yin
'''

def triangle(n):
    return int(n*(n+1)/2)

def pentagonal(n):
    return int(n*(3*n -1)/2)

def hexagonal(n):
    return int(n*(2*n - 1))

def find_t_p_h():
    triangle_set = {1}
    pentagonal_set = {1}
    hexagonal_set = {1}
    n = 2
    while True:
        triangle_set.add(triangle(n))
        pentagonal_set.add(pentagonal(n))
        hexagonal_set.add(hexagonal(n))
        if triangle(n) in pentagonal_set and triangle(n) in hexagonal_set and triangle(n) > 40755:
            return triangle(n)
        else:
            n += 1
            
print(find_t_p_h())

'''
1533776805
'''