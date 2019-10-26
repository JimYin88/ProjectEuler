'''
Created on Jan 27, 2019

@author: Jim Yin
'''

prime_numbers = [2]

def prime_gen(nth_term):
    prime_number_count = 1
    while prime_number_count < nth_term:
        for i in range(3, 1000000000000000, 2):
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                prime_numbers.append(i)
                prime_number_count += 1
    return prime_numbers


if __name__ == '__main__':
    result =  prime_gen(3)

print(result)

