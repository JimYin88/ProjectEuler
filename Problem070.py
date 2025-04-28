# Created on Jun 11, 2022
#
# @author: Jim Yin


from tqdm import tqdm
from collections import Counter
import time


def euler_totient(n):
    result = n
    p = 2
    while p * p <= n:
        if n % p == 0:
            while n % p == 0:
                n //= p
            result -= result // p
        p += 1
    if n > 1:
        result -= result // n
    return result


def prob_187():

    min_ratio = float('inf')
    min_totient = 1

    for i in tqdm(range(2, 10**7)):
        tol = euler_totient(i)
        if Counter(str(tol)) == Counter(str(i)):
            if i/tol < min_ratio:
                min_ratio = i/tol
                min_totient = i

    return min_totient


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_187())
    end_time = time.perf_counter()
    print(f'Time taken = {round(end_time - start_time, 4)} sec')


# 8319823
# Time taken = 543.9251 sec
