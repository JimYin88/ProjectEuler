# Created on Jun 2, 2022
#
# @author: Jim Yin

import time

def triangle(n):
    """
    :param n: nth member of the triangle number series
    :return: value of the nth member
    """
    return int(n*(n+1)/2)


def pentagonal(n):
    """
    :param n: nth member of the pentagonal number series
    :return: value of the nth member
    """
    return int(n*(3*n -1)/2)


def hexagonal(n):
    """
    :param n: nth member of the hexagonal number series
    :return: value of the nth member
    """
    return int(n*(2*n - 1))


def prob_045():
    """
    :return: the solution to Problem 45 in Project Euler
    """
    triangle_set = {1}
    pentagonal_set = {1}
    hexagonal_set = {1}
    n = 2
    while True:
        triangle_set.add(triangle(n))
        pentagonal_set.add(pentagonal(n))
        hexagonal_set.add(hexagonal(n))
        if triangle(n) in pentagonal_set and triangle(n) in hexagonal_set and triangle(n) > 40755:
            return triangle(n)
        else:
            n += 1


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_045())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 1533776805
# Time taken = 0.09843769999999999 sec
