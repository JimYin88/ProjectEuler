# Created on Jan 27, 2019
#
# @author: Jim Yin

def fib_gen():
    '''Generates a sequence of fibbonacci numbers'''
    a = 0
    b = 1
    while True:
        a, b = b, a+b
        yield a


def number_of_digit(n):
    return len(str(n))


def fib_first(ndigit):
    '''Find the first fibbonacci number with ndigit'''
    counter01 = 0     
    for x in fib_gen():
        counter01 += 1
        if number_of_digit(x) >= ndigit:
            print(counter01)
            break


def main():
    fib_first(1000)


if __name__ == '__main__':
    main()


# 4782
