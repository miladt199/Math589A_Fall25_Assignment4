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
  * Modify the Python wrapper, so that `solve_system` accepts a keyword parameter `scale`
    and passes it to C code.
  * Modify `main.c` so that the C code driver does not crash. I will check!
  * Provide Python driver `main.py` exercising the wrapper with
    several combinations of parameters.
  * Change documentation to reflect the above code modifications.



# How will your code be run by autograder?
  * I will run the Makefile
  * Make sure not to leave imports of unnecessary Python packages
    because the virtual machine supports only numpy. If you need a
    package, ask me to include it.
  * I will call your function `solve_system` and check the returned
    values against my code.
  
