# Created on Jun 2, 2022
#
# @author: Jim Yin

import time


square_digit_chain_dict = {1: 1, 89: 89}


def square_digit_chain(n):
    d = sum(int(d) ** 2 for d in str(n))
    if d in square_digit_chain_dict:
        return square_digit_chain_dict[d]
    nn = d
    while nn != 1 and nn != 89:
        nn = sum(int(x) ** 2 for x in str(nn))
    square_digit_chain_dict[d] = nn
    return nn


def prob_092(n):
    return sum(1 for i in range(1, n) if square_digit_chain(i) == 89)


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_092(n=10**7))
    end_time = time.perf_counter()
    print(f"Time taken = {round(end_time - start_time, 2)} sec")


# 8581146
# Time taken = 22.8 sec
