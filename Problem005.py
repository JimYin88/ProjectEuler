'''
Created on Jan 27, 2019

@author: Jim Yin
'''

'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20
'''

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a


def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


if __name__ == '__main__':
    result = 1
    for x in range(1,21):
        result = lcm(result, x)

print(result)

    