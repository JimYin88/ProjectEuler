# Created on Jun 14, 2022
#
# @author: Jim Yin

import time 
import math


def prob_099():
    
    lines = []
    with open('p099_base_exp.txt') as f:
        for line in f:
            x, y = line.replace('\n', '').split(',')
            lines.append([int(x), int(y)])
           
    result = [[idx, l[1]*math.log(l[0])] for idx, l in enumerate(lines)]
    final_result = sorted(result, key = lambda a: a[1], reverse=True)
    
    print(final_result[0][0]+1)
    

if __name__ == '__main__':
    start_time = time.perf_counter()
    prob_099()
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')
    

# 709
# Time taken = 0.002004700000000012 sec

