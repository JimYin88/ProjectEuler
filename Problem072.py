# Created on Jun 10, 2022
#
# @author: Jim Yin


import time


def find_factor(n):
    for i in range(2, int(n ** 0.5 + 1)):
        if n % i == 0:
            return i
    return n


def find_factors(n):
    factors = []
    while n != 1:
        fac = find_factor(n)
        if fac not in factors:
            factors.append(fac)
        n /= fac
    return factors


def totient(n):
    for factor in find_factors(n):
        n = n * (factor - 1) / factor

    return int(n)


def prob_072():

    result = 0
    for i in range(2, 1000001):
        result += totient(i)

    return result


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_072())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 303963552391
# Time taken = 19.91409370000474 sec
