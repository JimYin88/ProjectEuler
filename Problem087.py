# Created on March 22, 2025
#
# @author: Jim Yin


import time
from sympy import isprime


def prob_087(target=50_000_000):

    limit = int(target**(1/2))

    primes = [x for x in range(limit) if isprime(x)]

    prime_power_set = set()

    for i in primes:
        for j in primes:
            for k in primes:
                num = i**2 + j**3 + k**4
                if num > target:
                    break
                else:
                    prime_power_set.update([num])

    return len(prime_power_set)


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_087(target=50_000_000))
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 1097343
# Time taken = 0.9645949000259861 sec
