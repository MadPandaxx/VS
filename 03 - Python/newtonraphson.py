def f(x, A):
    return x**2 - A
def f_prime(x):
    return 2 * x
def newton_raphson(A, x1, tolerance=0.001, max_iterations=1000):
    iteration = 0 
    while True:
        xi = x1 - f(x1, A) / f_prime(x1)
        if abs(f(xi, A)) <= tolerance or iteration >= max_iterations:
            break
        x1 = xi 
        iteration += 1
    return xi, iteration

tiga_digit_terakhir_nim = 45

A = tiga_digit_terakhir_nim

x1 = 1.0

solution, iterations = newton_raphson(A, x1)

print("Solusi persamaan x^2 - {} = 0 adalah: {:.5f}".format(A, solution))
print("Iterasi yang diperlukan:", iterations)




