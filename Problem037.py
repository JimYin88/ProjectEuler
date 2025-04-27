# Created on May 26, 2022
#
# @author: Jim Yin


# The number 3797 has an interesting property. Being prime itself,
# it is possible to continuously remove digits from left to right,
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly, we can work from right to left: 3797, 379, 37, and 3.
#
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
#
# NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.


import time
from sympy import isprime


def sieve_of_eratosthenes(limit):
    """Generate prime numbers up to a given limit using the Sieve of Eratosthenes."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, limit + 1, start):
                sieve[multiple] = False

    for num in range(limit + 1):
        if sieve[num]:
            yield num


def trunctable(num):

    if len(str(num)) == 1:
        return False

    for t in range(len(str(num)) - 1):
        if not isprime(int(str(num)[t + 1:])):
            return False

    for t in range(len(str(num)) - 1):
        if not isprime(int(str(num)[0:-(t + 1)])):
            return False

    return True


def prob_037(n_prime=11):

    counter = 0
    result = 0
    primes = sieve_of_eratosthenes(10**6)

    prime = next(primes)

    while counter < n_prime:
        if trunctable(prime):
            counter += 1
            result += prime
        prime = next(primes)

    return result


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_037(n_prime=11))
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 748317
# Time taken = 0.35166209998715203 sec
