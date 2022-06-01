'''
Created on May 28, 2022

@author: Jim Yin
'''

'''
Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.

Peter and Colin roll their dice and compare totals: the highest total wins. The result is a draw if the totals are equal.

What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg
'''

peter = [sum((a, b, c, d, e, f, g, h, i)) for a in range(1, 5) for b in range(1, 5) for c in range(1, 5) for d in range(1, 5) for e in range(1, 5) for f in range(1, 5) for g in range(1, 5) for h in range(1, 5) for i in range(1, 5)]
peter_dict = dict()
for p in peter:
    if p not in peter_dict:
        peter_dict[p] = 1
    else:
        peter_dict[p] += 1

colin = [sum((a, b, c, d, e, f)) for a in range(1, 7) for b in range(1, 7) for c in range(1, 7) for d in range(1, 7) for e in range(1, 7) for f in range(1, 7)]
colin_dict = dict()
for c in colin:
    if c not in colin_dict:
        colin_dict[c] = 1
    else:
        colin_dict[c] += 1

peter_list = list(peter_dict.items())
colin_list = list(colin_dict.items())

p_win = sum(pv*cv for (p, pv) in peter_list for (c, cv) in colin_list if p > c)
c_win = sum(pv*cv for (p, pv) in peter_list for (c, cv) in colin_list if p < c)
tied = sum(pv*cv for (p, pv) in peter_list for (c, cv) in colin_list if p == c)

print(round((p_win/(p_win+c_win+tied)), 7))

'''
0.5731441
'''