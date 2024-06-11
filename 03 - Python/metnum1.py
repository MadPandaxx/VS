import numpy as np
import scipy.linalg as linalg

def solve_spl(method, A, b):
    if method == "gauss":
        return gauss_elimination(A, b)
    elif method == "gauss-jordan":
        return gauss_jordan_elimination(A, b)
    elif method == "lu":
        return lu_decomposition(A, b)
    else:
        print("Invalid method")
        return None

def gauss_elimination(A, b):
    return np.linalg.solve(A, b)

def gauss_jordan_elimination(A, b):
    aug_matrix = np.hstack([A, b.reshape(-1, 1)])
    row, col = 0, 0

    while True:
        i, j = np.unravel_index(aug_matrix[row:, col:].argmax(), aug_matrix[row:, col:].shape)
        i += row
        j += col

        if aug_matrix[i, j] == 0:
            col += 1
            if col == aug_matrix.shape[1] - 1:
                return aug_matrix[:, -1]
        else:
            aug_matrix[[row, i]] = aug_matrix[[i, row]]
            aug_matrix[row] = aug_matrix[row] / aug_matrix[row, j]

            for i in range(row + 1, aug_matrix.shape[0]):
                aug_matrix[i] -= aug_matrix[i, j] * aug_matrix[row]

            row += 1
            col += 1

            if row == aug_matrix.shape[0] or col == aug_matrix.shape[1] - 1:
                return aug_matrix[:, -1]

def lu_decomposition(A, b):
    lu, piv = linalg.lu_factor(A)
    x = linalg.lu_solve((lu, piv), b)
    return x

# Example usage:
A = np.array([[2, 1, -1],
              [-3, -1, 2],
              [-2, 1, 2]])

b = np.array([8, -11, -3])

method = input("Enter the method (gauss, gauss-jordan, lu): ")

solution = solve_spl(method, A, b)
print("Solution:", solution)
print("Solution:", solution)

check_solution(A, b)

if method == 'gauss-jordan':
    inverse = find_inverse(A)
    print("Inverse of A:")
    print(inverse)
