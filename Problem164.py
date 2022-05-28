'''
Created on May 27, 2022

@author: JimYi
'''


'''
How many 20 digit numbers n (without any leading zero) exist such that no three consecutive digits of n have a sum greater than 9?
'''

list03 = [[x, y, z, 1] for x in range(1,10) for y in range(10) for z in range(10) if x+y+z <= 9]

dict03 = dict()
for x, y, z, t in list03:
    if (y, z) not in dict03:
        dict03[(y, z)] = t
    else:
        dict03[(y, z)] += t

def add_digit(dict_o, n):
    while n < 20:
        list_i = [[x, y, z, dict_o[(x, y)]] for x, y in dict_o for z in range(10) if x+y+z <= 9]
        dict_n = dict()
        for x, y, z, t in list_i:
            if (y, z) not in dict_n:
                dict_n[(y, z)] = t
            else:
                dict_n[(y, z)] += t
    
        dict_o = dict_n
        n += 1
    
    return dict_o
        
final_dict = add_digit(dict03, 3) 

print(sum((final_dict[(x, y)] for (x, y) in final_dict)))    
    
'''
378158756814587
'''