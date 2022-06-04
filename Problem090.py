'''
Created on Jun 4, 2022

@author: Jim Yin
'''

die_requirement = ['04', '06', '16', '25', '36', '46', '64', '81']
die_dict = {(0,): [1], (1, ): [0]}


for i in die_requirement:
    new_dict = {}
    for c, j in enumerate(i):
        for k in die_dict.keys():
            if c == 0:
                new_dict[(k + (int(j),))] = die_dict[k] + [int(i[1])]
            if c == 1:
                new_dict[(k + (int(j),))] = die_dict[k] + [int(i[0])]

    die_dict = new_dict

def die_generator2(r):
    return [(str(a) + str(b) + str(c) + str(d) + str(e) + str(f)) for a in range(0, 5) for b in range(a+1, 6) \
            for c in range(b+1, 7) for d in range(c+1, 8) for e in range (d+1, 9) for f in range(e+1, 10) \
            if set(r).issubset(set([a, b, c, d, e, int(str(f).replace('9', '6'))]))]    
   
result = []
for e, k in enumerate(die_dict):
    combo = [(x, y) for x in die_generator2(k) for y in die_generator2(die_dict[k])]
    result.extend(combo)

unique = set(result)

print(int(len(unique)/2))
