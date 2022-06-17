# Created on Jun 14, 2022
#
# @author: Jim Yin


import time
import numpy as np
from tqdm import tqdm


lines = []
with open('p082_matrix.txt') as f:
    for line in f:
        lines.append([int(x) for x in line.replace('\n', '').split(',')])


start_time = time.perf_counter()
layers = len(lines)

lines = np.array(lines)
matrix = lines.copy()

            
for j in tqdm(range(1, layers)):
    for i in range(layers):
        matrix[i][j] = min([(lines[i][j] + matrix[k][j-1] if k == i else lines[i][j] + matrix[k][j-1] + sum(lines[k:i, j])) \
                            if k <= i else lines[i][j] + matrix[k][j-1] + sum(lines[i+1:k+1, j]) for k in range(layers)])


print(min(matrix[:, 79]))
end_time = time.perf_counter()

print(f'Time taken = {end_time - start_time} sec')


# 260324
# Time taken = 2.8626396 sec
