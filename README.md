# fp-energy-saving
Analyzing energy saving by reducing the precision of Floating-point arithmetic operations

This is one part of the tool chain for estimating the engergy saving for any program written in C.
The method for saving energy is using less precision for Floating-point arithmetic operations.
To achive this, the following steps are completed sequentially:
1. Converting the orginal program written in C to MPFR program (the program that use MPFR operations for any Floating-point operations.
2. Using [https://github.com/minhhn2910/RandomHeuristicSearch] to search for the acceptable precisions of each variable of the MPFR program, given the expected error bound from users.
3. Use this tool to estimate the energy saving by counting the number of mpfr operations that executed at a lower precision. 

Input:
	1. MPFR program that use gcov [https://gcc.gnu.org/onlinedocs/gcc/Gcov.html] tool to count frequency of each line of code
	2. The search result from [https://github.com/minhhn2910/RandomHeuristicSearch]
Output:
	Estimate how much energy will be saved if we have the flexible hardware that enables multiple-precision floating-point computations
