# Created on Jun 22, 2022
#
# @author: Jim Yin

import time


def prob_032():
    number_max = 987654321

    result = []
    for i in range(1, int(number_max**0.5)):
        for j in range(i+1, number_max):
            if len(str(i))+ len(str(j)) + len(str(i*j)) > 9:
                break
            if len(str(i))+ len(str(j)) + len(str(i*j)) == 9:
                if set(str(i) + str(j) + str(i*j)) == set(['1', '2', '3', '4', '5', '6', '7', '8', '9']):
                    result.append(i*j)
      
    return sum(set(result))


if __name__ == '__main__':
    start_time = time.perf_counter()
    print(prob_032())
    end_time = time.perf_counter()
    print(f'Time taken = {end_time - start_time} sec')
    

# 45228
# Time taken = 0.17579470000000003 sec
        
        