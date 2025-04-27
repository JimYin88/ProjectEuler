# Created on Jun 2, 2022
#
# @author: Jim Yin


import time


def n_repeating_digits(n):

    remainders = set()
    remainder = 1

    while True:
        if remainder in remainders:
            return len(remainders)
        if remainder > n:
            remainder = remainder % n
        elif remainder == n:
            return 0
        elif remainder == 0:
            return 0
        elif remainder < n:
            remainders.update([remainder])
            remainder *= 10


def prob_026():

    max_repeating_digit = 0
    max_number = 0

    for i in range(1, 1000):
        d = n_repeating_digits(i)
        if d > max_repeating_digit:
            max_repeating_digit = d
            max_number = i

    return max_number


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_026())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 983
# Time taken = 0.04359469999326393 sec
