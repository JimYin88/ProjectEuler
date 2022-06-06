# Created on Jan 27, 2019
#
# @author: Jim Yin

import time
start_time = time.perf_counter()


def collatzcount(n):
    result = 1
    if n == 1:
        return result
    while n > 1:
        if n %2 == 0:
            n /= 2
            result += 1
        else:
            n = 3*n + 1
            result += 1
    return result


def main():
    result = [(i, collatzcount(i)) for i in range(1, 10**6)]
    highest_collatzcount = sorted(result, key = lambda x: x[1])
    print(highest_collatzcount[-1][0])
    
    # highestcollatzcount = 1
    # highestcollatz = 1
    #
    # for i in range(1000000):
    #     x = collatzcount(i)
    #     if x > highestcollatzcount:
    #         highestcollatzcount = x
    #         highestcollatz = i
    #
    # print(highestcollatz)


if __name__ == '__main__':
    main()


# 837799


end_time = time.perf_counter()
print(f'Time taken = {end_time - start_time} sec')


# Time taken = 38.1480969 sec
