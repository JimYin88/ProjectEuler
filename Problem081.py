# Created on Feb 9, 2019
#
# @author: Jim Yin


import time


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


def prob_081():

    matrix2 =[]
    with open('0081_matrix.txt') as f:
        for line in f.readlines():
            matrix2.append(line)

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

    return path_pre[layer, layer]


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_081())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')


# 427337
# Time taken = 0.019742100004805252 sec
