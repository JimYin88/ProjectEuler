# Created on April 15, 2025
#
# @author: Jim Yin


import time
from fractions import Fraction


def prob_033():

    result = 1
    for i in range(10, 100):
        for j in range(i+1, 100):
            if int(str(j)[1]) != 0:
                if str(i)[1] == str(j)[0]:
                    if int(str(i)[0])/int(str(j)[1]) == i/j:
                        if i % 11 != 0:
                            result *= Fraction(i, j)

    return result.denominator


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_033())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 100
# Time taken = 0.002448599989293143 sec
