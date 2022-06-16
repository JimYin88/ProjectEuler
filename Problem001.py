# Created on Jan 24, 2019
#
# @author: Jim Yin

import time


def prob_001():
    print(sum([x for x in range(1000) if x % 5 == 0 or x % 3 == 0]))


if __name__ == '__main__':
    start_time = time.perf_counter()
    prob_001()
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 233168
# Time taken = 0.00018719999999999848 sec

