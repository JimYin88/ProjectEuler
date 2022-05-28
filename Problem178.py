'''
Created on May 28, 2022

@author: Jim Yin
'''

list02 = [[x, y, 0, 0, 1] for x in range(1,10) for y in range(x-1, x+2, 2) if y <= 9 and y >=0]

for n, (x, y, a, b, t) in enumerate(list02):
    if x == 0 or y == 0:
        list02[n] = [x, y, 1, b, t]
    if x == 9 or y == 9:
        list02[n] = [x, y, a, 1, t]

dict02 = dict()
for x, y, a, b, t in list02:
    if (y, a, b) not in dict02:
        dict02[(y, a, b)] = t
    else:
        dict02[(y, a, b)] += t

def add_digit(dict_o, n):
    total = 0
    while n < 40:
        list_i = [[x, y, a, b, dict_o[(x, a, b)]] for x, a, b in dict_o for y in range(x-1, x+2, 2) if y <= 9 and y >=0]
        for m, (x, y, a, b, t) in enumerate(list_i):
            if y == 0:
                list_i[m] = [x, y, 1, b, t]
            if y == 9:
                list_i[m] = [x, y, a, 1, t]
        
        dict_n = dict()
        for x, y, a, b, t in list_i:
            if (y, a, b) not in dict_n:
                dict_n[(y, a, b)] = t
            else:
                dict_n[(y, a, b)] += t
                
        dict_o = dict_n
        n += 1

        total += sum(dict_o[(y, a, b)] for (y, a, b) in dict_o if a==1 and b==1)
        # print(n, sum(dict_o[(y, a, b)] for (y, a, b) in dict_o), sum(dict_o[(y, a, b)] for (y, a, b) in dict_o if a==1 and b==1), total)

    return total

print(add_digit(dict02, 2)) 
    
'''
126461847755
'''