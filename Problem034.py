# Created on May 25, 2022
#
# @author: Jim Yin


import time


def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i

    return result


def digit_factorials(n):
    return n == sum(factorial(int(i)) for i in str(n))


def prob_034(lower_limit, upper_limit):
    return sum(i for i in range(lower_limit, upper_limit) if digit_factorials(i))


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_034(3, factorial(10)))
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 40730
# Time taken = 17.810290900000837 sec
