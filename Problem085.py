# Created on Jun 1, 2022
#
# @author: Jim Yin

import time


def grid_number(m, n):
    return sum((m-i)*(n-j) for i in range(m) for j in range(n))
    
    
def find_grid(rect):
    min_diff = rect
    for m in range(1, 101):
        n = 1
        rect_calc = 0
        while rect_calc < rect + min_diff:
            rect_calc = grid_number(m, n)
            if abs(rect_calc - rect) < min_diff:
                m_diff = m 
                n_diff = n 
                min_diff = abs(rect_calc - rect)
            n += 1

    return m_diff*n_diff


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(find_grid(2000000))
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


'''
2772
Time taken = 2.6672639 sec
'''