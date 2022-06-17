'''
Created on Feb 9, 2019

@author: Jim Yin
'''

matrix1 = [[131, 673, 234, 103, 18],
           [201, 96, 342, 965, 150],
           [630, 803, 746, 422, 111],
           [537, 699, 497, 121, 956],
           [805, 732, 524, 37, 331]]


matrix2 =[]
with open('p081_matrix.txt') as f:
    for line in f.readlines():
        matrix2.append(line)
 
 
def strip0(string1):
    string1 = string1.replace('/n', '')
    if string1[0:3] == '000':
        return int(string1[3:])
    elif string1[0:2] == '00':
        return int(string1[2:])
    elif string1[0:1] == '0':
        return int(string1[1:])
    else:
        return int(string1)
    
       
matrix3 = []
for strings in matrix2:
    l = strings.split(',')
    next_line = []
    for num in l:
        next_line.append(strip0(num))
    matrix3.append(next_line)


layer = 79
path_init = {(0, 0): 4445}
path_pre = path_init
path_next = []

for i in range(158):
    for x, y in path_pre:
        if x+1 <= layer:
            path_next.append([(x+1, y), path_pre[(x,y)] + matrix3[x+1][y]])
        if y+1 <= layer:
            path_next.append([(x, y+1), path_pre[(x,y)] + matrix3[x][y+1]])

    path_next_dict = {}

    for j in path_next:
        if j[0] not in path_next_dict:
            path_next_dict[j[0]] = j[1]
        else:
            path_next_dict[j[0]] = min(path_next_dict[j[0]], j[1])

    path_pre = path_next_dict
    path_next = []

print(path_pre[layer, layer])






# c = [b[i].split(',') for i in range(80)]
# d = [[int(c[i][j]) for j in range(80)] for i in range(80)]
# print(d[0][79])
#
# print(sum([d[0][i] for i in range(80)]))
#
#
# pathmin = [[4445]]
#
# for i in range(79):
#     pathmin.append([0 for x in range(i+2)])
#     for j in range(i+2):
#         if j == 0:
#             pathmin[i+1][j] = pathmin[i][j]+d[i-j+1][j]
#         elif j == i + 1:
#             pathmin[i+1][j] = pathmin[i][j-1]+d[i-j+1][j]
#         else:
#             pathmin[i+1][j] = min(pathmin[i][j]+d[i-j+1][j], pathmin[i][j-1]+d[i-j+1][j])
#     print(min(pathmin[-1]))
#
#
# linereducer = 0
# for i in range(80, 82):
#     pathmin.append([0 for x in range(159 - i)])
#
#
#     linereducer += 1 
#     for j in range(159 - i):
#         pathmin[i][j] = min(pathmin[i-1][j]+d[i-j-linereducer][j+linereducer], pathmin[i-linereducer][j+1]+d[i-j-1][j+linereducer])
#
#     print(min(pathmin[-1]))   
#
#
# print(pathmin[-2])     
# print(pathmin[-1])     
#
#
