# Created on April 11, 2025
#
# @author: Jim Yin


import time


def prob_028(spiral_size=1001):

    size = 1
    diagonal = 1
    last = 1

    for _ in range(3, spiral_size + 2, 2):
        size += 2
        if size == 3:
            corner1 = last + 2
            corner2 = corner1 + size - 1
            corner3 = corner2 + size - 1
            corner4 = corner3 + size - 1
            diagonal += corner1 + corner2 + corner3 + corner4
            last = corner4
        else:
            corner1 = last + size - 1
            corner2 = corner1 + size - 1
            corner3 = corner2 + size - 1
            corner4 = corner3 + size - 1
            diagonal += corner1 + corner2 + corner3 + corner4
            last = corner4

    return diagonal


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_028())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 669171001
# Time taken = 0.00034169999707955867 sec
