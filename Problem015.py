# Created on Jun 10, 2022
#
# @author: JimYi


path_init = {(0, 0): 1}
path_pre = path_init
path_next = []
 

for i in range(20):
    
    for x, y in path_pre:
        path_next.append([(x+1, y), path_pre[(x,y)]])
        path_next.append([(x, y+1), path_pre[(x,y)]])
    
    path_next_dict = {}
    for j in path_next:
        if j[0] not in path_next_dict:
            path_next_dict[j[0]] = j[1]
        else:
            path_next_dict[j[0]] += j[1]

    path_pre = path_next_dict
    path_next = [] 


for i in range(20):
    
    for x, y in path_pre:
        if x+1 <= 20:
            path_next.append([(x+1, y), path_pre[(x,y)]])
        if y+1 <= 20:
            path_next.append([(x, y+1), path_pre[(x,y)]])
    
    path_next_dict = {}
    for j in path_next:
        if j[0] not in path_next_dict:
            path_next_dict[j[0]] = j[1]
        else:
            path_next_dict[j[0]] += j[1]

    path_pre = path_next_dict
    path_next = [] 

    
print(path_pre[(20, 20)])

