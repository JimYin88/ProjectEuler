# Created on Jun 3, 2022
#
# @author: Jim Yin

import time
from sympy import isprime


def find_spiral_primes():
    layer = 3
    number_prime = 0
    number_nonprime = 1

    while True:
        lower_right = layer**2
        lower_left = layer**2 - layer + 1
        upper_left = layer**2 - 2*layer + 2
        upper_right = layer**2 - 3*layer + 3

        diagonal = [lower_right, lower_left, upper_left, upper_right]

        for n in diagonal:
            if isprime(n):
                number_prime += 1
            else:
                number_nonprime += 1

        if number_prime/(number_prime + number_nonprime) < 0.1:
            return layer
        else:
            layer += 2


if __name__ == '__main__':
    time_start = time.perf_counter()
    print(find_spiral_primes())
    time_end = time.perf_counter()
    print(f"time taken = {time_end - time_start} sec")


'''
26241
time taken = 0.2502003999999999 sec
'''
