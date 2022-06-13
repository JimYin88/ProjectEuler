# Created on Jun 1, 2022
#
# @author: Jim Yin

# import time
# import math
#
#
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
#
#
# prime_list = [x for x in prime_gen(2, 10 ** 6)]
#
#
# def circularprime(n):
#     for i in range(len(str(n))):
#         if int(str(n)[i:]+str(n)[0:i]) not in prime_list:
#             return False
#     return True
#
#
# def main():
#     print(sum(1 for x in prime_list if circularprime(x)))
#
#
# if __name__ == '__main__':
#     start_time = time.perf_counter()
#     main()
#     end_time = time.perf_counter()
#     print(f'Time taken = {end_time - start_time} sec')


# 55
# Time taken = 114.7745275 sec


import time
import math
from multiprocessing import Process, Manager


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


prime_list = [x for x in prime_gen(2, 10 ** 6)]


def circularprime(n):
    for i in range(len(str(n))):
        if int(str(n)[i:] + str(n)[0:i]) not in prime_list:
            return False
    return True


def prob_035(lowerlimit, upperlimit, return_dict):
    return_dict[(lowerlimit, upperlimit)] = int(sum(1 for x in prime_list[lowerlimit:upperlimit] if circularprime(x)))


if __name__ == '__main__':
    manager = Manager()
    return_dict = manager.dict()
    processes = []
    start_time = time.perf_counter()

    process1 = Process(target=prob_035, args=(0, 10000, return_dict))
    process1.start()
    processes.append(process1)

    process2 = Process(target=prob_035, args=(10000, 20000, return_dict))
    process2.start()
    processes.append(process2)

    process3 = Process(target=prob_035, args=(20000, 30000, return_dict))
    process3.start()
    processes.append(process3)

    process4 = Process(target=prob_035, args=(30000, 40000, return_dict))
    process4.start()
    processes.append(process4)

    process5 = Process(target=prob_035, args=(40000, 50000, return_dict))
    process5.start()
    processes.append(process5)

    process6 = Process(target=prob_035, args=(50000, 60000, return_dict))
    process6.start()
    processes.append(process6)

    process7 = Process(target=prob_035, args=(60000, 70000, return_dict))
    process7.start()
    processes.append(process7)

    process8 = Process(target=prob_035, args=(70000, len(prime_list), return_dict))
    process8.start()
    processes.append(process8)

    for p in processes:
        p.join()  # wait for finish of jobs

    print(sum(return_dict.values()))

    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')

# 55
# Time taken = 28.4167057 sec
