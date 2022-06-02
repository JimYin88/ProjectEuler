'''
Created on Jun 1, 2022

@author: Jim Yin
'''

passcode = [319, 680, 180, 690, 129, 620, 762, 689, 762, 318, 368, 710, 720, 710, 629, 168, 160, 689, 716, 731, 736,
            729, 316, 729, 729, 710, 769, 290, 719, 680, 318, 389, 162, 289, 162, 718, 729, 319, 790, 680, 890, 362,
            319, 760, 316, 729, 380, 319, 728, 716]

passcode_string = [str(x) for x in passcode]

passcode_integer_set = set()

for j in passcode_string:
    for k in j:
        if int(k) not in passcode_integer_set:
            passcode_integer_set.add(int(k))
    
passcode_full = ''

while max(len(r) for r in passcode_string):
    for i in passcode_integer_set:
        if str(i) in passcode_full:
            continue
        if max(x.index(str(i)) for x in passcode_string if str(i) in x) == 0:
            passcode_full = passcode_full + str(i)
            passcode_string = [s.replace(str(i), '') for s in passcode_string]

print(passcode_full)

'''
73162890
'''