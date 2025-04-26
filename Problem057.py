# Created on March 22, 2025
#
# @author: Jim Yin


import time
import fractions


def prob_057(n=1000):

    frac = fractions.Fraction(0.5)
    counter = 0

    for i in range(n):
        term = fractions.Fraction(1 + frac)
        if len(str(term.numerator)) - len(str(term.denominator)) > 0:
            counter += 1
        frac = 1/(2 + frac)

    return counter


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_057(n=1000))
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')

# 153
# Time taken = 0.010292999999364838 sec
