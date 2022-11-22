# Speed Sum Comparison
Make a comparison of performances between multiple implementations (always with main in Python).

We have the exact same behaviour for all implementations. Then for each implementation we quantify the time it took to process the iteration.

## Comparison
```txt
Operating System: EndeavourOS
KDE Plasma Version: 5.26.2
KDE Frameworks Version: 5.99.0
Qt Version: 5.15.6
Kernel Version: 6.0.2-arch1-1 (64-bit)
Graphics Platform: X11
Processors: 4 × Intel® Core™ i5-6300U CPU @ 2.40GHz
Memory: 15.0 Gio of RAM
Graphics Processor: Mesa Intel® HD Graphics 520
Manufacturer: HP
Product Name: HP EliteBook 840 G3

---Benchmark with 100000000 iterations---
Full Python:
 8.914542536999988 s
Iteration in C:
 5.364402272000007 s
Full C:
 0.1767641100000219 s
Full Fortran:
 0.011275610999973651 s

```

## Requirements
### Interpreter/Compilator
- [Python 3](https://www.python.org/downloads/);
- [gFortran](https://fortran-lang.org/en/learn/os_setup/install_gfortran/).

### Modules
#### numpy
If you don't have numpy installed:
```bash
pip install numpy
```
**or**
```bash
python -m pip install numpy
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

## Additionnal informations
The system informations written at the beginning of the benchmark are pre-inserted from `system.txt` file. Modify it to your need.

## Run the script
```bash
python main.py
```
