'''
Created on Jun 2, 2022

@author: Jim Yin
'''

def generate_pentagonals(x):
    for i in range(1, x+1):
        yield int(i * (3 * i - 1) / 2)


def find_pentagonals():
    pentagonals = set(generate_pentagonals(3000))
    for x in pentagonals:
        for y in pentagonals:
            if x + y in pentagonals and x - y in pentagonals:
                return x - y
                

print(find_pentagonals())

'''
5482660
'''
