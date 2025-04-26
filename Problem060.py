from sympy import isprime
import time

start_time = time.perf_counter()


def prime_generator():
    """Generate an infinite sequence of prime numbers."""
    yield 2
    num = 3
    while True:
        if isprime(num):
            yield num
        num += 2


def sieve_of_eratosthenes(limit):
    """Generate prime numbers up to a given limit using the Sieve of Eratosthenes."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime numbers

    for start in range(2, int(limit**0.5) + 1):
        if sieve[start]:
            for multiple in range(start*start, limit + 1, start):
                sieve[multiple] = False

    for num in range(limit + 1):
        if sieve[num]:
            yield num


s1 = set()
s2 = s1
# gen = sieve_of_eratosthenes(20000)
gen = prime_generator()
counter = 0

while counter < 2000:
    prime = next(gen)
    for i in s1:
        cond = True
        for j in i:
            if not isprime(int(str(j)+str(prime))):
                cond = False
                break
            if not isprime(int(str(prime)+str(j))):
                cond = False
                break
        if cond:
            s2.update([i + (prime, )])
    s2.update([(prime, )])
    s1 = s2.copy()
    counter += 1
    # if counter % 100 == 0:
    #     print(counter)

# print(max(len(t) for t in s1))

lowest = [t for t in s1 if len(t) == 5]

print(sum(lowest[0]))

end_time = time.perf_counter()

print(f'Time taken = {end_time - start_time} sec')

#
# if __name__ == '__main__':
#     start_time = time.perf_counter()
#     print(prob_019())
#     end_time = time.perf_counter()
#     print(f'Time taken = {end_time - start_time} sec')

# 26033
# Time taken = 225.5432104999927 sec

