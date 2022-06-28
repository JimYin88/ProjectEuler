# Created on Jun 22, 2022
#
# @author: Jim Yin


from tqdm import tqdm
from collections import Counter
import time
import math
from sympy import isprime


def prime_gen(lowerlimit, upperlimit):
    num = max(2, lowerlimit)
    if num == 2:
        yield num
    if num % 2 == 0:
        num += 1
    for i in range(num, upperlimit, 2):
        if isprime(i):
            yield i
        
        


# def prime_gen(lowerlimit, upperlimit):
#     num = max(2, lowerlimit)
#     if num == 2:
#         yield num
#         num += 1
#
#     if num == 3:
#         yield num
#         num += 2
#
#     if num % 2 == 0:
#         num += 1
#
#     while num < upperlimit:
#         isprime = True
#
#         for x in range(3, int(math.sqrt(num)) + 1, 2):
#             if num % x == 0:
#                 isprime = False
#                 break
#
#         if isprime:
#             yield num
#
#         num += 2


def prob_049():
    prime_list = [x for x in prime_gen(1000, 10**4)]
    length = len(prime_list)

    result = []

    for i in tqdm(range(length - 2)):
        for j in range(i + 1, length - 1):
            for k in range(j + 1, length):
                if prime_list[j] - prime_list[i] == prime_list[k] - prime_list[j]:
                    if Counter(str(prime_list[i])) == Counter(str(prime_list[j])) and Counter(str(prime_list[i])) == Counter(str(prime_list[k])):
                        result.append(int(str(prime_list[i]) + str(prime_list[j]) + str(prime_list[k])))
                
    print(result[-1])
    
    
if __name__ == '__main__':
    start_time = time.perf_counter()
    prob_049()
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 296962999629
# Time taken = 45.2133934 sec
