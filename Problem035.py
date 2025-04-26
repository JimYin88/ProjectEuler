# Created on April 25, 2025
#
# @author: Jim Yin


from sympy import isprime
import time


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


def prime_rotation(n):

    if len(str(n)) == 1:
        return True

    for i in range(len(str(n))):
        if not isprime(int(str(n)[i:] + str(n)[:i])):
            return False

    return True


def prob_035(limit=10**6):

    primes = sieve_of_eratosthenes(limit+100)

    prime = next(primes)
    counter = 0

    while prime < limit:
        if prime_rotation(prime):
            counter += 1
        prime = next(primes)

    return counter


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_035(10**6))
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 55
# Time taken = 1.445053100003861 sec
