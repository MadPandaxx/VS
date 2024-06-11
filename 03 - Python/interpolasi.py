import numpy as np

# Titik data (VCE, IC)
data_points = np.array([
    [1.0, 2.0],
    [2.0, 4.0],
    [3.0, 6.0]
])

def newton_polynomial(x, data_points):
    n = len(data_points)
    divided_diff = np.zeros((n, n))
    divided_diff[:,0] = data_points[:,1]

    # Menghitung divided differences
    for j in range(1, n):
        for i in range(n-j):
            divided_diff[i][j] = (divided_diff[i+1][j-1] - divided_diff[i][j-1]) / (data_points[i+j][0] - data_points[i][0])

    # Evaluasi polinomial Newton pada x
    result = divided_diff[0,0]
    for i in range(1, n):
        term = divided_diff[0,i]
        for j in range(i):
            term *= (x - data_points[j][0])
        result += term

    return result

def lagrange_polynomial(x, data_points):
    n = len(data_points)
    result = 0.0

    # Membangun polinomial Lagrange
    for i in range(n):
        term = data_points[i][1]
        for j in range(n):
            if j != i:
                term *= (x - data_points[j][0]) / (data_points[i][0] - data_points[j][0])
        result += term

    return result

# VCE yang ingin kita hitung IC-nya
VCE_value = 2.5

# Menghitung menggunakan metode Newton
IC_newton = newton_polynomial(VCE_value, data_points)

# Menghitung menggunakan metode Lagrange
IC_lagrange = lagrange_polynomial(VCE_value, data_points)

IC_newton, IC_lagrange