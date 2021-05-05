import time
from math import pi, sqrt, e, pow



def loop_fact(n):
    res = 1
    for i in range(n, 1, -1):
        res *= i
    return res

def power_mod(base, k):
    k_bin = bin(k)[2:-1][::-1] # remove prefix, last bit and reversed binary
    total = 1 
    expand = base
    for bi_di in k_bin: # first digit ignored
        expand *= expand
        # print(expand)
        if bi_di == "1":
            total = (total * expand) 
    if k % 2 == 1:
        # because we remove the first digit
        """ Feel like could be optimized but naaahhh """
        total *= base
    return total


def stirling_formula(n):
    return sqrt(2*pi*n) * power_mod((n/e), n)


def stirling_formula_comparison(n):
    print(f"We are comparing the calculation of {n}! by looping and by Sterling's approximation :")
    print('-'*80, '\n')
    start_time = time.time()
    r1 = loop_fact(n)
    t1 = time.time() - start_time
    print(f"The value from looping : {r1}")
    print(f"Execution time : {t1}\n")

    start_time = time.time()
    r2 = stirling_formula(n)
    t2 = time.time() - start_time
    print(f"The value from Stirling's approximation : {r2}")
    print(f"Execution time : {t2}")

stirling_formula_comparison(150)