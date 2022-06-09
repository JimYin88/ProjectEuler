'''
Created on Jan 27, 2019

@author: Jim Yin
'''

def filllength(s):
    if len(s) == 1:
        return '00' + s
    elif len(s) == 2:
        return '0' + s
    else:
        return s
    

def digitsetcount(s):
    digitset = set()
    for d in s:
        digitset = digitset | set(d)
    return len(digitset)    
    

d234 = [filllength(str(x)) for x in range(1000) if x % 2 == 0]
d345 = [filllength(str(x)) for x in range(1000) if x % 3 == 0]
d456 = [filllength(str(x)) for x in range(1000) if x % 5 == 0]
d567 = [filllength(str(x)) for x in range(1000) if x % 7 == 0]
d678 = [filllength(str(x)) for x in range(1000) if x % 11 == 0]
d789 = [filllength(str(x)) for x in range(1000) if x % 13 == 0]
d8910 = [filllength(str(x)) for x in range(1000) if x % 17 == 0]


d2345 = []
for x in d234:
    for y in d345:
        if x[1:3] == y[0:2] and digitsetcount(x + y[2:]) == 4:            
            d2345.append(x + y[2:])
            
print(len(d2345))

d23456 = []
for x in d2345:
    for y in d456:
        if x[2:4] == y[0:2] and digitsetcount(x + y[2:]) == 5:            
            d23456.append(x + y[2:])
            
print(len(d23456))


d234567 = []
for x in d23456:
    for y in d567:
        if x[3:5] == y[0:2] and digitsetcount(x + y[2:]) == 6:            
            d234567.append(x + y[2:])
            
print(len(d234567))
    

d2345678 = []
for x in d234567:
    for y in d678:
        if x[4:6] == y[0:2] and digitsetcount(x + y[2:]) == 7:            
            d2345678.append(x + y[2:])
            
print(len(d2345678))
          

d23456789 = []
for x in d2345678:
    for y in d789:
        if x[5:7] == y[0:2] and digitsetcount(x + y[2:]) == 8:            
            d23456789.append(x + y[2:])
            
print(len(d23456789))
     

d2345678910 = []
for x in d23456789:
    for y in d8910:
        if x[6:8] == y[0:2] and digitsetcount(x + y[2:]) == 9:            
            d2345678910.append(x + y[2:])
            
print(len(d2345678910))

print(d2345678910)

results = []
for i in range(9):
    for j in d2345678910:
        if digitsetcount(str(i)+j) == 10:
            results.append(int(str(i)+j))

print(sum(results)) 
               
'''
16695334890
'''
