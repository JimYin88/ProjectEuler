# Created on April 21, 2025
#
# @author: Jim Yin


import time
from itertools import permutations


def prob_068():

    result = []

    for i in range(13, 17):

        target = i

        perms = permutations([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

        counter = 0
        while counter < 3628800:
            p = next(perms)
            if p[0] + p[1] + p[2] == target:
                if p[3] + p[2] + p[4] == target:
                    if p[5] + p[4] + p[6] == target:
                        if p[7] + p[6] + p[8] == target:
                            if p[9] + p[8] + p[1] == target:
                                if min(p[0], p[3], p[5], p[7], p[9]) == p[0]:
                                    number = int(str(p[0]) + str(p[1]) + str(p[2]) + str(p[3]) + str(p[2])
                                                 + str(p[4]) + str(p[5]) + str(p[4]) + str(p[6]) + str(p[7])
                                                 + str(p[6]) + str(p[8]) + str(p[9]) + str(p[8]) + str(p[1]))
                                elif min(p[0], p[3], p[5], p[7], p[9]) == p[3]:
                                    number = int(str(p[3]) + str(p[2]) + str(p[4]) + str(p[5]) + str(p[4])
                                                 + str(p[6]) + str(p[7]) + str(p[6]) + str(p[8]) + str(p[9])
                                                 + str(p[8]) + str(p[1]) + str(p[0]) + str(p[1]) + str(p[2]))
                                elif min(p[0], p[3], p[5], p[7], p[9]) == p[5]:
                                    number = int(
                                        str(p[5]) + str(p[4]) + str(p[6]) + str(p[7]) + str(p[6]) + str(
                                            p[8])
                                        + str(p[9]) + str(p[8]) + str(p[1]) + str(p[0]) + str(p[1]) + str(
                                            p[2])
                                        + str(p[3]) + str(p[2]) + str(p[4]))
                                elif min(p[0], p[3], p[5], p[7], p[9]) == p[7]:
                                    number = int(
                                        str(p[7]) + str(p[6]) + str(p[8]) + str(p[9]) + str(p[8]) + str(
                                            p[1])
                                        + str(p[0]) + str(p[1]) + str(p[2]) + str(p[3]) + str(p[2]) + str(
                                            p[4])
                                        + str(p[5]) + str(p[4]) + str(p[6]))
                                else:
                                    number = int(
                                        str(p[9]) + str(p[8]) + str(p[1]) + str(p[0]) + str(p[1]) + str(
                                            p[2])
                                        + str(p[3]) + str(p[2]) + str(p[4]) + str(p[5]) + str(p[4]) + str(
                                            p[6])
                                        + str(p[7]) + str(p[6]) + str(p[8]))

                                if number < 10 ** 16:
                                    result.append(number)
            counter += 1

    return max(result)


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_068())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 6531031914842725
# Time taken = 4.726656800005003 sec
