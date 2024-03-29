# Created on Jun 3, 2022
#
# @author: Jim Yin


import time
time_start = time.perf_counter()

words = []

with open("p042_words.txt") as f:
    line = f.read()
    words = line.strip().replace('"','').split(',')

letter_map = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, \
              'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, \
              'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}


def word_score(a_string):
    return sum(letter_map[letter] for letter in a_string)


triangle_numbers = [int(n*(n+1)/2) for n in range(40)]

print(sum(1 for w in words if word_score(w) in triangle_numbers))

'''
162
'''

time_end = time.perf_counter()
print(f"time taken = {time_end-time_start} sec")

'''
time taken = 0.0031686000000000075 sec
'''