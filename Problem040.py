'''
Created on May 31, 2022

@author: Jim Yin
'''

def d_num(digit):
    decimal_number_string = ''
    string_length = 0
    num = 1
    while string_length <= digit:
        decimal_number_string = decimal_number_string + str(num)
        num += 1
        string_length += len(str(num))
        
    return decimal_number_string

d = 1000000
print(int(d_num(d)[0])*int(d_num(d)[9])*int(d_num(d)[99])*int(d_num(d)[999])*int(d_num(d)[9999])*int(d_num(d)[99999]))


'''
210
'''





    