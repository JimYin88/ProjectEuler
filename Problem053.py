'''
Created on May 26, 2022

@author: Jim Yin
'''

'''
How many, not necessarily distinct, values of (n r) for 1 <= n <= 100 are greater than one-million?
'''

import math

print(sum(1 for n in range(1, 101) for r in range(1, n) if math.comb(n, r) > 1000000))

'''
4075
'''