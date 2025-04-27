# Created on April 20, 2025
#
# @author: Jim Yin


import time
from sympy.solvers.diophantine.diophantine import diop_DN


def prob_066(limit=1000):

    squares = [i**2 for i in range(1, int(limit**(1/2)) + 1)]
    d_candidates = [i for i in range(1, limit + 1) if i not in squares]

    result = []
    for d in d_candidates:
        ans = diop_DN(d, 1)
        result.append([d, ans[0][0]])

    d = 0
    max_value = 0

    for i in result:
        if i[1] > max_value:
            d = i[0]
            max_value = i[1]

    return d


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_066())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 661
# Time taken = 12.184974400006467 sec
