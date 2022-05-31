'''
Created on May 30, 2022

@author: Jim Yin
'''

'''
A particular school offers cash rewards to children with good attendance and punctuality. If they are absent for three consecutive days or late on more than one occasion then they forfeit their prize.

During an n-day period a trinary string is formed for each child consisting of L's (late), O's (on time), and A's (absent).

Although there are eighty-one trinary strings for a 4-day period that can be formed, exactly forty-three strings would lead to a prize:

OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
LAOO LAOA LAAO

How many "prize" strings exist over a 30-day period?
'''

attendance_possibility = ['L', 'O', 'A']

def late(a):
    if a == 'L':
        return 1
    else:
        return 0

list02 = [[x, y, 0, late(x) + late(y), 1] for x in attendance_possibility for y in attendance_possibility]

dict02 = dict()
for x, y, z, l, t in list02:
    if l > 1:
        continue
    elif x == y == z == 'A':
        continue
    elif (x, y, l) not in dict02:
        dict02[(x, y, l)] = t
    else:
        dict02[(x, y, l)] += t

list03 = [[x, y, a, l + late(a), dict02[(x, y, l)]] for x, y, l in dict02 for a in attendance_possibility]

dict03 = dict()

for x, y, z, l, t in list03:
    if l > 1:
        continue
    elif x == y == z == 'A':
        continue
    elif (y, z, l) not in dict03:
        dict03[(y, z, l)] = t
    else:
        dict03[(y, z, l)] += t

def add_digit(dict_o, n):
    while n < 30:
        list_i = [[x, y, a, l + late(a), dict_o[(x, y, l)]] for x, y, l in dict_o for a in attendance_possibility]

        dict_n = dict()
        for x, y, z, l, t in list_i:
            if l > 1:
                continue
            elif x == y == z == 'A':
                continue
            elif (y, z, l) not in dict_n:
                dict_n[(y, z, l)] = t
            else:
                dict_n[(y, z, l)] += t
                
        dict_o = dict_n
        n += 1

    return sum(dict_o[t] for t in dict_o)

print(add_digit(dict03, 3))

'''
1918080160
'''