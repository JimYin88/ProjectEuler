# Created on December 12, 2014
#
# @author: Jim Yin


# Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:
#
# 1634 = 1**4 + 6**4 + 3**4 + 4**4
# 8208 = 8**4 + 2**4 + 0**4 + 8**4
# 9474 = 9**4 + 4**4 + 7**4 + 4**4
# As 1 = 1**4 is not a sum it is not included.
#
# The sum of these numbers is 1634 + 8208 + 9474 = 19316.
#
# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


import time


def fifth_powers_of_digits(n):
    return n == sum(int(i)**5 for i in str(n))


def prob_030():
    return sum(i for i in range(2, 6*9**5) if fifth_powers_of_digits(i))


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_030())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 443839
# Time taken = 0.9498548000119627 sec
