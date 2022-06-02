'''
Created on Jun 2, 2022

@author: Jim Yin
'''

'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

def divisors(n):
    return sum(i for i in range(1, int(n/2)+1) if n % i == 0)

divisor_dict = {i: divisors(i) for i in range(1, 10000)}

result = []
for k in divisor_dict:
    if divisor_dict[k] not in divisor_dict:
        continue
    elif k != divisor_dict[k] and divisor_dict[divisor_dict[k]] == k:
        result.append(k)
        
print(sum(result))    
        
'''
31626
'''

        