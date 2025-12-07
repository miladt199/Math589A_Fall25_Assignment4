from fp_wrapper import solve_system


def run_example(x1_0, x2_0, tol, max_iter, scale):
    print("=" * 60)
    print(f"Initial guess: x1_0 = {x1_0}, x2_0 = {x2_0}")
    print(f"tol = {tol}, max_iter = {max_iter}, scale = {scale}")
    try:
        x1, x2, iters = solve_system(x1_0, x2_0, tol, max_iter, scale=scale)
        print(f"Converged in {iters} iterations.")
        print(f"Solution: x1 = {x1:.10f}, x2 = {x2:.10f}")
    except RuntimeError as e:
        print(f"Solver failed: {e}")


def main():
    # A few combinations of parameters
    run_example(0.5, 0.5, 1e-6, 1000, 0.1)   # original behavior
    run_example(0.5, 0.5, 1e-8, 2000, 0.05)  # smaller scale, tighter tol
    run_example(1.0, -1.0, 1e-6, 1000, 0.2)  # different initial guess + scale


if __name__ == "__main__":
    main()
