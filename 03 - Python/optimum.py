import math

def f(x):
    return 0.25  * x**4 - 1.1 * x**3 + 1.75 * x**2 -2 * x

def golden_section_search(f,x_L, x_U, tol=1e-6, max_iter=100):
    golden_ratio = (math.sqrt(5) - 1) / 2

    d = golden_ratio * (x_U - x_L)
    x1 = x_U - d
    x2 = x_L + d

    for i  in range(max_iter):
        if  abs(x_U - x_L) < tol:
            break

        f1 = f(x1)
        f2 = f(x2)

        if f1 < f2 :
            x_U = x2
        else:
            x_L = x1

        d = golden_ratio * (x_U - x_L)
        x1 = x_U - d
        x2 = x_L +  d

    x_optimum = (x_U + x_L) / 2
    return x_optimum, f(x_optimum)

x_L = -2
x_U = 4  

x_optimum, min_value = golden_section_search(f, x_L, x_U)

print("Nilai optimum x:", x_optimum)
print("Nilai Minimum f(x):", min_value)