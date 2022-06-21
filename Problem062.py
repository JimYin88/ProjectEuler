# Created on Jun 3, 2022
#
# @author: Jim Yin

import time


def prob_062(number_permutation):
    cubic_cache = {}
    num = 1
    while True:
        cubic = num**3
        permute = ''.join(sorted(str(cubic)))
        if permute not in cubic_cache:
            cubic_cache[permute] = [cubic]
        else:
            cubic_cache[permute].append(cubic)   
            
        if len(cubic_cache[permute]) == number_permutation:
            return min(cubic_cache[permute])
        else:
            num += 1


if __name__ == '__main__':
    time_start = time.perf_counter()
    print(prob_062(5))
    time_end = time.perf_counter()
    print(f"Time taken = {time_end - time_start} sec")


# 127035954683
# Time taken = 0.016483499999999984 sec
