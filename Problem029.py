# Created on April 10, 2025
#
# @author: Jim Yin


import time


def prob_029():

    return len(set((a ** b for a in range(2, 101) for b in range(2, 101))))


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_029())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 9183
# Time taken = 0.005575200004386716 sec
