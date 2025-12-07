import ctypes
import os

_here = os.path.abspath(os.path.dirname(__file__))
_libpath = os.path.join(_here, "libfixed_point.so")
_lib = ctypes.CDLL(_libpath)

# C signature:
# int fixed_point_solve(double x1_0, double x2_0, double scale,
#                       double tol, int max_iter,
#                       double *x1_out, double *x2_out, int *iters_out);
_lib.fixed_point_solve.argtypes = [
    ctypes.c_double,                  # x1_0
    ctypes.c_double,                  # x2_0
    ctypes.c_double,                  # scale
    ctypes.c_double,                  # tol
    ctypes.c_int,                     # max_iter
    ctypes.POINTER(ctypes.c_double),  # x1_out
    ctypes.POINTER(ctypes.c_double),  # x2_out
    ctypes.POINTER(ctypes.c_int)      # iters_out
]
_lib.fixed_point_solve.restype = ctypes.c_int


def solve_system(x1_0, x2_0, tol, max_iter, scale=0.1):
    x1_out = ctypes.c_double()
    x2_out = ctypes.c_double()
    iters_out = ctypes.c_int()

    rc = _lib.fixed_point_solve(
        x1_0,
        x2_0,
        scale,
        tol,
        max_iter,
        ctypes.byref(x1_out),
        ctypes.byref(x2_out),
        ctypes.byref(iters_out),
    )

    if rc != 0:
        # rc == 1 : did not converge
        # rc < 0  : invalid input
        raise RuntimeError(f"C solver error {rc}")

    return x1_out.value, x2_out.value, iters_out.value
