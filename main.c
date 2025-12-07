#include <stdio.h>
#include "fixed_point.h"

int main(void)
{
    double x1, x2;
    int iters;

    // initial guess
    double x1_0   = 0.5;
    double x2_0   = 0.5;
    double scale  = 0.1;    // same as original hard-coded value
    double tol    = 1e-6;
    int    max_it = 1000;

    int rc = fixed_point_solve(x1_0, x2_0, scale, tol, max_it, &x1, &x2, &iters);

    if (rc == 0) {
        printf("Converged:\n");
        printf("x1 = %.10f\n", x1);
        printf("x2 = %.10f\n", x2);
        printf("iterations = %d\n", iters);
    } else if (rc == 1) {
        printf("Did not converge in %d iterations.\n", iters);
        printf("Last iterate: x1 = %.10f, x2 = %.10f\n", x1, x2);
    } else {
        printf("Invalid input.\n");
    }

    return 0;
}
