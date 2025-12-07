#ifndef FIXED_POINT_H
#define FIXED_POINT_H

int fixed_point_solve(double x1_0, double x2_0, double scale,
                      double tol, int max_iter,
                      double *x1_out, double *x2_out, int *iters_out);

#endif
