'''
Created on Jun 11, 2022

@author: Jim Yin 
'''

from tqdm import tqdm
from collections import Counter
import math
from multiprocessing import Process, Manager
import time


def factors(n):
    remainder = n
    div = 2
    result = set()
    while remainder > 1:
        if remainder % div == 0:
            if div in result:
                remainder /= div
            else:
                result.add(div)
                remainder /= div
        else:
            if div == 2:
                div += 1
            else:
                div += 2
    
    return result



def prime_gen(lowerlimit, upperlimit):
    num = max(2, lowerlimit)
    if num == 2:
        yield num
        num += 1

    if num == 3:
        yield num
        num += 2

    if num % 2 == 0:
        num += 1

    while num < upperlimit:
        isprime = True

        for x in range(3, int(math.sqrt(num)) + 1, 2):
            if num % x == 0:
                isprime = False
                break

        if isprime:
            yield num

        num += 2


prime_list = [x for x in prime_gen(2, 1.01*10 ** 7)]


def factors2(n) :
    result = set()
    remainder = n
    for prime in prime_list:
        if remainder == 1:
            return result
        while remainder > 1:
            if remainder % prime == 0:
                if prime in result:
                    remainder /= prime
                else:
                    result.add(prime)
                    remainder /= prime
            else:
                break
            

def totient(n) :
    for factor in factors2(n) :
        n = n * (factor - 1) / factor
        
    return int(n)



def find_permutation(n):
    return Counter(str(n)) == Counter(str(totient(n)))


def totient_ratio(n):
    return n/totient(n)



def prob_070(upperlimit, lowerlimit, return_dict):
    lowest_totient_ratio = 2
    lowest_totient_number = 0

    for i in tqdm(range(upperlimit, lowerlimit, -1), mininterval = 1):
        if find_permutation(i):
            if totient_ratio(i) < lowest_totient_ratio:
                lowest_totient_ratio = totient_ratio(i)
                lowest_totient_number = i

    return_dict[(upperlimit, lowerlimit)] = (lowest_totient_number, lowest_totient_ratio)  


if __name__ == '__main__':
    manager = Manager()
    return_dict = manager.dict()
    processes = []
    start_time = time.perf_counter()

    process1 = Process(target=prob_070, args=(10000000, 9750000, return_dict))
    process1.start()
    processes.append(process1)

    process2 = Process(target=prob_070, args=(9750000, 9500000, return_dict))
    process2.start()
    processes.append(process2)

    process3 = Process(target=prob_070, args=(9500000, 9250000, return_dict))
    process3.start()
    processes.append(process3)

    process4 = Process(target=prob_070, args=(9250000, 9000000, return_dict))
    process4.start()
    processes.append(process4)

    process5 = Process(target=prob_070, args=(9000000, 8750000, return_dict))
    process5.start()
    processes.append(process5)

    process6 = Process(target=prob_070, args=(8750000, 8500000, return_dict))
    process6.start()
    processes.append(process6)

    process7 = Process(target=prob_070, args=(8500000, 8250000, return_dict))
    process7.start()
    processes.append(process7)

    process8 = Process(target=prob_070, args=(8250000, 8000000, return_dict))
    process8.start()
    processes.append(process8)

    for p in processes:
        p.join()  # wait for finish of jobs

    result = return_dict.values()
    
    print(sorted(result, key = lambda x: x[1])[0][0])

    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 8123821
# Time taken = 3684.9560842 sec
    

