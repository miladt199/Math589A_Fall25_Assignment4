import ctypes
import os

_here = os.path.abspath(os.path.dirname(__file__))
_libpath = os.path.join(_here, "libfixed_point.so")
_lib = ctypes.CDLL(_libpath)

_lib.fixed_point_solve.argtypes = [
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_double,
    ctypes.c_int,
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_double),
    ctypes.POINTER(ctypes.c_int)
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
        raise RuntimeError(f"C solver error {rc}")

    return x1_out.value, x2_out.value, iters_out.value
