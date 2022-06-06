# Created on Jun 3, 2022
#
# @author: Jim Yin


import time


def nine_digit_gen(n):
    ndigit = 0
    multiplier = 1
    n_string = ''
    while ndigit < 9:
        n_string += str(n * multiplier)
        ndigit = len(n_string)
        multiplier += 1
    if ndigit > 9:
        return 0
    elif ''.join(sorted(n_string)) == '123456789':
        return int(n_string)
    else:
        return 0


def main():
    print(max(nine_digit_gen(i) for i in range(10000)))


if __name__ == '__main__':
    time_start = time.perf_counter()
    main()
    time_end = time.perf_counter()
    print(f'Time taken = {time_end - time_start} sec')


# 932718654
# Time taken = 0.017682200000000002 sec
