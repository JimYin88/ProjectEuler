# Created on May 21, 2022
#
# @author: Jim Yin


# 2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#
# What is the sum of the digits of the number 2**1000?


import time


def main():
    n_string = str(2 ** 1000)
    print(sum(int(d) for d in n_string))


if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 1366
# Time taken = 9.409999999999974e-05 sec

