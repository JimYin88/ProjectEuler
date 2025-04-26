# Created on March 6, 2015
#
# @author: Jim Yin


import time


def abundant(n):
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    result.remove(n)

    return sum(result) > n


def prob_023(limit=28123):

    abundant_numbers = [num for num in range(1, limit) if abundant(num)]
    sum_two_abundant_numbers = {i+j for i in abundant_numbers for j in abundant_numbers}

    return sum([i for i in range(1, limit) if i not in sum_two_abundant_numbers])


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_023(28123))
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 4179871
# Time taken = 3.715199300000677 sec
