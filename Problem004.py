'''
Created on Jan 27, 2019

@author: JimYin
'''


def palindrome(n):
    s = str(n)
    if s == s[::-1]:
        return True
    else:
        return False
    

if __name__ == '__main__':
    l = [x * y for x in range(100,1000) for y in range(100,1000) if palindrome(x*y)]

print(max(l))

    