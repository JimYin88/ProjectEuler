# Created on May 24, 2022
#
# @author: Jim Yin


# If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.
#
# Not all numbers produce palindromes so quickly. For example,
#
# 349 + 943 = 1292,
# 1292 + 2921 = 4213
# 4213 + 3124 = 7337
#
# That is, 349 took three iterations to arrive at a palindrome.
#
# Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome.
# A number that never forms a palindrome through the reverse and add process is called a Lychrel number.
# Due to the theoretical nature of these numbers, and for the purpose of this problem,
# we shall assume that a number is Lychrel until proven otherwise. In addition you are given that for
# every number below ten-thousand, it will either (i) become a palindrome in less than fifty iterations,
# or, (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome.
# In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome:
# 4668731596684224866951378664 (53 iterations, 28-digits).
#
# Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.
#
# How many Lychrel numbers are there below ten-thousand?
#
# NOTE: Wording was modified slightly on 24 April 2007 to emphasize the theoretical nature of Lychrel numbers.


import time


def palindrome_int(n):
    return str(n)[::-1] == str(n)


def lychrel_check(n):
    count = 0
    last = n
    while count < 100:
        summation = int(str(last)[::-1]) + last
        if palindrome_int(summation):
            return False
        else:
            last = summation
            count += 1
    return True


def prob_055():
    print(sum(1 for n in range(10000) if lychrel_check(n)))


if __name__ == '__main__':
    start_time = time.perf_counter()
    prob_055()
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 249
# Time taken = 0.07576779999999994 sec

