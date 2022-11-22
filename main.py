import timeit
import numpy as np
import sumfortran

n = 100_000_000

def sum_while():
    """
    Sum using full Python
    """
    val = 0
    i = 0
    while i < n:
        val += i
        i += 1
    return val

def sum_for_range():
    """
    Sum using iteration in C
    """
    val = 0
    for i in range(n):
        val += i
    return val

def sum_numpy():
    """
    Sum using pure C
    """
    return np.sum(np.arange(n))

def p_timeit(f, msg: str):
    print(msg, timeit.timeit(f, number=1), 's')

if __name__ == "__main__":
    print(open("./system.txt", 'r').read())
    print(f"\n---Benchmark with {n} iterations---")
    p_timeit(msg="Full Python:\n", f=sum_while)
    p_timeit(msg="Iteration in C:\n", f=sum_for_range)
    p_timeit(msg="Full C:\n", f=sum_numpy)
    p_timeit(msg="Full Fortran:\n", f=sumfortran.sum)
