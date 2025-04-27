# Created on Jun 16, 2022
#
# @author: Jim Yin


from sympy import isprime
import time


def pandigital_prime(n):
    if '0' in str(n):
        return False

    return set(str(n)) == {str(i) for i in range(1, len(str(n))+1)}


def prob_041():
    prime_list = (i for i in range(9_999_999, 999_999, -2) if isprime(i))
    # Need to check only 7 digits prime since 8 and 9-digits pandigitals are
    # divisible by 3.

    while True:
        i = next(prime_list)
        if pandigital_prime(i):
            return i


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_041())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 7652413
# Time taken = 3.2882332999997743 sec
