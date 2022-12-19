# Speed Sum Comparison
Make a comparison of performances between multiple implementations (always with main in Python).

We have the exact same behaviour for all implementations. Then for each implementation we quantify the time it took to process the iteration.

## Comparison
```txt
---Benchmark with 100000000 iterations---
Full Python:
 10.325035517000288 s
Iteration in C:
 5.541200206000212 s
Full C:
 0.1813937619999706 s
Full Fortran:
 0.011550537000402983 s

--- Time with compilation
Cython:
 9.545514385000388 s
Numba:
 0.17455050199987454 s

--- Time without compilation
Numba:
 3.0470000638160855e-06 s

```

The results are separated in 3 parts:
- The first part is the time it took to process the iteration for each implementation;
- The second part is the time it took to compile the Cython and Numba implementations and then process the iteration;
- The third part is the time it took to process the iteration for the Numba implementation without compilation (because it was previously compiled).

## Implementations
The Python implementation is the simplest one. It is the reference implementation. It is the one we want to compare the other implementations to.

For **pure C** implementation, we use exclusively the numpy module so if you want to use it, you need your code to be compatible with numpy.

For **Fortran** implementation, we use Fortran 95, then we compile it with f2py. If you want to use it, you require your code to be Fortran 95 compatible.

**Cython** and **Numba** implementations are compiled at runtime. So it's basically pure Python code that is compiled at runtime. These implementations are interesting because they are as fast to write as pure Python code.

Specifically for **Numba**, we use the `@jit` decorator to compile the function. It is the fastest way to compile a function with Numba. But it is also the most restrictive. If you want to use it, you require your code to be compatible with Numba. Once compiled, it won't need to be compiled again. That is why the third part of the benchmark is so fast.

As for **Cython**, you need to compile the code each time before running it. But it is more flexible than Numba. You can use it with any Python code.

## Requirements
### Interpreter/Compilator
- [Python 3](https://www.python.org/downloads/);
- [gFortran](https://fortran-lang.org/en/learn/os_setup/install_gfortran/).

### Modules
- numpy
- cython
- numba

To install the modules:
```bash
pip install -r requirements.txt
```
**or**
```bash
python -m pip install -r requirements.txt
```

## Compile FORTRAN module for your architecture/os
To compile FORTRAN module:
```bash
f2py -c sumfortran.f95 -m sumfortran
```
**or**
```bash
python -m numpy.f2py -c sumfortran.f95 -m sumfortran
```

## Run the script
```bash
python main.py
```
