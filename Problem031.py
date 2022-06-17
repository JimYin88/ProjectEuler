# Created on Jun 1, 2022
#
# @author: Jim Yin

import time
from collections import defaultdict


def pro_031():
    """
    Find the solution of Problem 31 in Project Euler.
    :return: Answer: 73682
    """
    coins =[200, 100, 50, 20, 10, 5, 2, 1]
    result_old = defaultdict(int)
    result_old[200] = 1    

    for c in coins:
        result_next = defaultdict(int)
        for rem in result_old:
            number_of_c = 0
            while rem - c*number_of_c >= 0:
                result_next[rem - c*number_of_c] += result_old[rem]
                number_of_c += 1

        result_old = result_next
        
    print(result_old[0])


if __name__ == '__main__':
    start_time = time.perf_counter()
    pro_031()
    end_time = time.perf_counter()
    print(f'time taken: {end_time - start_time} sec')


# 73682
# time taken: 0.007597500000000007 sec
