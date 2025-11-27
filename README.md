# Math589A_Assignment4
	
  * Implementing Fixed Point iteration 2D in C.
  * Implementing Python wrapper using ctypes package.

# What is given?
  * A basic implementation of Fixed Point Method in C: files `fixed_point.c` and `fixed_point.h`. It only solves a specific system.
  * A Python wrapper which calls C code to solve the system: file `fp_wrapper.py`. It includes the necessary declarations of types and calling sequence. It provides the function `solve_system` which allows passing initial conditions, tolerance and maximum number of iterations to C code.
  * A basic C driver of for the C implementation: `main.c`


# What is required?
  * Modify C code to accept an additional parameter of type `double` called `scale`
  * Replace the hard-coded constant 0.1 in the system of being solved with `scale`.
  * Modify the Python wrapper to accept a keyword parameter `scale`
    and pass it to C code.
  * Modify `main.c` so that the C code driver does not crash. I will check!
  * Change documentation to reflect the code modification



