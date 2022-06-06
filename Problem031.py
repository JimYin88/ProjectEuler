# Created on Jun 1, 2022
#
# @author: Jim Yin

import time


def main():
    coins =[200, 100, 50, 20, 10, 5, 2, 1]
    result_old = {200: 1}

    for c in coins:
        result_next = dict()
        for rem in result_old:
            number_of_c = 0
            while rem - c*number_of_c >= 0:
                if (rem - c*number_of_c) not in result_next:
                    result_next[rem - c*number_of_c] = result_old[rem]
                else:
                    result_next[rem - c*number_of_c] += result_old[rem]

                number_of_c += 1

        result_old = result_next

    print(result_old[0])


if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f'time taken: {end_time - start_time} sec')


# 73682
# time taken: 0.009263399999999998 sec
