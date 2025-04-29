'''
Created on Jun 16, 2022

@author: Jim Yin
'''

import math

result = sorted([b**p for b in range(1, 100) for p in range(1, 100) if len(str(b**p)) == p])
print(result)
print(len(result))
