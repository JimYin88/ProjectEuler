# Created on Jun 2, 2022
#
# @author: Jim Yin


import time

number_partitions_dict = {0: 1, 1: 1, 2: 2}


def n_partitions(n):
    
    global number_partitions_dict

    if n < 0:
        number_partitions_dict[n] = 0
        return 0

    if n in number_partitions_dict:
        return number_partitions_dict[n]

    sm = 0

    for k in range(1, n + 1):
        n1 = n - int(k * (3 * k - 1) / 2)
        n2 = n - int(k * (3 * k + 1) / 2)
        sm += (-1) ** (k + 1) * (n_partitions(n1) + n_partitions(n2))
        if n1 <= 0:
            break

    number_partitions_dict[n] = sm
    return sm


def prob_078():

    start = 2
    while True:
        partitions = n_partitions(start)
        if partitions % 1000000 == 0:
            return start
        else:
            start += 1


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_078())
    end_time = time.perf_counter()
    print(f'Time taken = {round(end_time - start_time, 4)} sec')


# 55374
# Time taken = 8.707 sec
