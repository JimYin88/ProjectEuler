# Created on Jun 2, 2022
#
# @author: Jim Yin


import time


def main():
    rem_prev = {100: 1}

    for i in range(99, 0, -1):
        rem_next = {}
        for rem in rem_prev:
            num_subtract = 0
            while rem - num_subtract*i >= 0:
                if (rem - num_subtract*i) not in rem_next:
                    rem_next[rem - num_subtract*i] = rem_prev[rem]
                else:
                    rem_next[rem - num_subtract*i] += rem_prev[rem]

                num_subtract += 1

        rem_consolidate = {}
        for k in rem_next:
            if k not in rem_consolidate:
                rem_consolidate[k] = rem_next[k]
            else:
                rem_consolidate[k] += rem_next[k]

        rem_prev = rem_consolidate
         
    print(rem_prev[0])


if __name__ == '__main__':
    start_time = time.perf_counter()
    main()
    end_time = time.perf_counter()
    print(f"Time taken = {end_time - start_time} sec")


# 190569291
# Time taken = 0.010388600000000012 sec
