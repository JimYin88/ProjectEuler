# Created on Jun 2, 2022
#
# @author: Jim Yin

import time

square_digit_chain_dict = {}

def square_digit_chain(n):
    d = sum(int(d)**2 for d in str(n))
    if d in square_digit_chain_dict:
        return d, square_digit_chain_dict[d]
    nn = d
    while nn != 1 and nn != 89:
        nn = sum(int(x)**2 for x in str(nn))
    square_digit_chain_dict[d] = nn
    return d, nn


def main():
    print(sum(1 for i in range(1, 10**7) if square_digit_chain(i)[1] == 89))


if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Time taken = {round(end_time - start_time, 2)} sec")
    

# 8581146
# Time taken = 36.74 sec

