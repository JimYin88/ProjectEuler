# Created on Jun 2, 2022
#
# @author: Jim Yin

import time


def generate_pentagonals(x):
    for i in range(1, x+1):
        yield int(i * (3 * i - 1) / 2)


def find_pentagonals():
    pentagonals = set(generate_pentagonals(3000))
    for x in pentagonals:
        for y in pentagonals:
            if x + y in pentagonals and x - y in pentagonals:
                return x - y


def prob_044():
    print(find_pentagonals())


if __name__ == '__main__':
    start_time = time.perf_counter()
    prob_044()
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 5482660
# Time taken = 0.608291 sec

