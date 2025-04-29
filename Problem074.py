'''
Created on Jun 13, 2022

@author: JimYi
'''
from functools import wraps, cache
from tqdm import tqdm


def memo(func):
    cache = {}                             # Stored subproblem solutions
    @wraps(func)                           # Make wrap look like func
    def wrap(*args):                       # The memoized wrapper
        if args not in cache:              # Not already computed?
            cache[args] = func(*args)      # Compute & cache the solution
        return cache[args]                 # Return the cached solution
    return wrap


@cache
def factorial(n):
    if n == 0:
        return 1
    result = 1
    rem = n
    while rem > 1:
        result *= rem
        rem -= 1
    return result


@cache
def sum_of_digit_factorial(n):
    return sum(factorial(int(d)) for d in str(n))


def chain_length(n):
    chain = [n]
    last_number = n
    while True:
        next_number = sum_of_digit_factorial(last_number)
        if next_number not in chain:
            chain.append(next_number)
            last_number = next_number
        else:
            return len(chain)
        

print(sum(1 for i in tqdm(range(1000000)) if chain_length(i) == 60))


# 402
