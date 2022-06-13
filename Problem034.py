# Created on May 25, 2022
#
# @author: Jim Yin


# 145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
#
# Find the sum of all numbers which are equal to the sum of the factorial of their digits.
#
# Note: As 1! = 1 and 2! = 2 are not sums they are not included.

# import time
# from multiprocessing import Process, Manager
#
#
# def factorial(n):
#     result = 1
#     for i in range(1, n+1):
#         result *= i
#
#     return result
#
#
# def digit_factorials(n):
#     return n == sum(factorial(int(i)) for i in str(n))
#
#
# def prob_034(lower_limit, upper_limit):
#     print(sum(i for i in range(lower_limit, upper_limit) if digit_factorials(i)))
#
#
# if __name__ == '__main__':
#     start_time = time.perf_counter()
#     prob_034(3, factorial(10))
#     end_time = time.perf_counter()
#     print(f'Time taken = {end_time - start_time} sec')


# 40730
# Time taken = 21.9549248 sec


import time
from multiprocessing import Process, Manager


def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i

    return result


def digit_factorials(n):
    return n == sum(factorial(int(i)) for i in str(n))


def prob_034(lower_limit, upper_limit, return_dict):
    return_dict[(lower_limit, upper_limit)] = sum(i for i in range(lower_limit, upper_limit) if digit_factorials(i))
    return (sum(i for i in range(lower_limit, upper_limit) if digit_factorials(i)))


if __name__ == '__main__':
    manager = Manager()
    return_dict = manager.dict()
    processes = []
    start_time = time.perf_counter()

    process1 = Process(target=prob_034, args=(3, 1000000, return_dict))
    process1.start()
    processes.append(process1)

    process2 = Process(target=prob_034, args=(1000000, 2000000, return_dict))
    process2.start()
    processes.append(process2)

    process3 = Process(target=prob_034, args=(2000000, 3000000, return_dict))
    process3.start()
    processes.append(process3)

    process4 = Process(target=prob_034, args=(3000000, factorial(10), return_dict))
    process4.start()
    processes.append(process4)

    for p in processes:
        p.join()  # wait for finish of jobs

    print(sum(return_dict.values()))

    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')

# 40730
# Time taken = 12.9384628 sec
