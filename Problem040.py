# Created on May 31, 2022
#
# @author: Jim Yin

import time


def dnum(digit):
    dec_num_str = ''
    str_len = 0
    num = 1
    while str_len <= digit:
        dec_num_str = dec_num_str + str(num)
        num += 1
        str_len += len(str(num))
        
    return dec_num_str


def prob_040():
    d = 1000000
    print(int(dnum(d)[0])*int(dnum(d)[9])*int(dnum(d)[99])*int(dnum(d)[999])*int(dnum(d)[9999])*int(dnum(d)[99999]))


if __name__ == '__main__':
    start_time = time.perf_counter()
    prob_040()
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 210
# Time taken = 0.8030874 sec




    