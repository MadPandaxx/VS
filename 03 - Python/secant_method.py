#Secant Method
def f(x, A):
    return x**2 - A

def secant_method(A, x1, x2, tolerance=0.001, max_iterations=1000):
    iteration = 0
    while True:
        xi = x2 - f(x2, A) * (x2 - x1) / (f(x2, A) - f(x1, A))
        if abs(f(xi, A)) <= tolerance or iteration >= max_iterations:
            break
        x1 = x2
        x2 = xi
        iteration += 1
    return xi, iteration
tiga_digit_terakhir_nim = 45

A = tiga_digit_terakhir_nim

x1 = 0
x2 = 10

solution, iterations = secant_method(A, x1, x2)

print("Solusi persamaan x^2 - {} = 0 adalah: {:.5f}".format(A, solution))
print("Iterasi yang diperlukan:", iterations)






