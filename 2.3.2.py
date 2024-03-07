import itertools
def primes():
    a = 1
    while True:
        a += 1
        ndiv = 2
        for i in range(2, a):
            if a % i == 0:
                ndiv += 1
                break
        if ndiv == 2:
            yield a
            


print(list(itertools.takewhile(lambda x : x <= 31, primes())))
# [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]