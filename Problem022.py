'''
Created on May 26, 2022

@author: Jim Yin
'''


names = open('p022_names.txt', 'r')
namestr = names.readline()

namelist = namestr.replace('"','').split(',')
namelist.sort()

def letter_value(s):
    d = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}
    return d[s]

def word_value(w):
    return sum(letter_value(s) for s in w)

print(sum(word_value(name)*(o+1) for o, name in enumerate(namelist)))

'''
871198282
'''