import timeit
import numpy as np
import cython
import numba
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

@cython.cfunc
@cython.boundscheck(False)
@cython.inline
def sum_while_cython():
    """
    Sum using full Python read by Cython.
    During interpretation, the function is compiled to C.
    """
    val = 0
    i = 0
    while i < n:
        val += i
        i += 1
    return val

@numba.jit
def sum_while_numba():
    """
    Sum using full Python read by Numba.
    During interpretation, the function is compiled to LLVM (machine code).
    """
    val = 0
    i = 0
    while i < n:
        val += i
        i += 1
    return val

def p_timeit(f, msg: str):
    print(msg, timeit.timeit(f, number=1), 's')

if __name__ == "__main__":
    print(f"\n---Benchmark with {n} iterations---")
    p_timeit(msg="Full Python:\n", f=sum_while)
    p_timeit(msg="Iteration in C:\n", f=sum_for_range)
    p_timeit(msg="Full C:\n", f=sum_numpy)
    p_timeit(msg="Full Fortran:\n", f=sumfortran.sum)
    print("\n--- Time with compilation")
    p_timeit(msg="Cython:\n", f=sum_while_cython)
    p_timeit(msg="Numba:\n", f=sum_while_numba)
    print("\n--- Time without compilation")
    p_timeit(msg="Numba:\n", f=sum_while_numba)
