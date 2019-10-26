'''
Created on Jan 27, 2019

@author: JimYi
'''


'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

if __name__ == '__main__':
    primenumber = 600851475143
    divider = 2
    result = []
    while primenumber > 1:
        if primenumber % divider == 0:
            result.append(divider)
            primenumber /= divider
        else: 
            divider += 1

print(max(result))

    
