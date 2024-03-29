# Created on May 26, 2022
#
# @author: Jim Yin

import time


def letter_value(s):
    d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, \
         'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    return d[s]


def word_value(w):
    return sum(letter_value(s) for s in w)


if __name__ == '__main__':
    start_time = time.perf_counter()
    with open('p022_names.txt', 'r') as names:
        namestr = names.readline()
        namelist = namestr.replace('"','').split(',')
        namelist.sort()
        
    print(sum(word_value(name)*(o+1) for o, name in enumerate(namelist)))
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')
    

# 871198282
# Time taken = 0.0365356 sec
