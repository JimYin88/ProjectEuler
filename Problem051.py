# Created on April 25, 2025
#
# @author: Jim Yin


from itertools import permutations
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


def find_all_indices(string, char):
    return [index for index, c in enumerate(string) if c == char]


def repeating_digits_0_1(n, digit):
    return str(n).count(str(digit)) > 2


def number_variation(n, position):
    result = []
    number_string = str(n)
    for number_replacement in range(10):
        number = ''
        for idx, digit in enumerate(number_string):
            if idx in position:
                number += str(number_replacement)
            else:
                number += str(digit)

        result.append(int(number))

    return result


def prob_051():
    primes = sieve_of_eratosthenes(10 ** 6)

    while True:
        prime = next(primes)

        if repeating_digits_0_1(prime, 1):
            positions = find_all_indices(str(prime), str(1))
            for n_digit in range(2, len(positions) + 1):
                perm = permutations(positions, n_digit)
                for p in perm:
                    nums = number_variation(n=prime, position=p)
                    if len([i for i in nums if isprime(i)]) >= 8 and \
                    len(str([i for i in nums if isprime(i)][0])) == len(str([i for i in nums if isprime(i)][-1])):
                        return [i for i in nums if isprime(i)][0]


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_051())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 121313
# Time taken = 0.8357813999900827 sec
