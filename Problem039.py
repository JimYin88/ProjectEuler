'''
Created on Jun 22, 2022

@author: JimYi
'''

import time
import math
from collections import Counter 


result = []
for i in range(1, 334):
    for j in range(i+1, 500):
        k = math.sqrt((i**2 + j **2))
        if i+j+k > 1000:
            break
        if k == math.floor(k):
            result.append(int(i+j+k))
 
final_result = Counter(result)
print(final_result.most_common(1)[0][0])