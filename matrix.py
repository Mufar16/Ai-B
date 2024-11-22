import numpy as np

# Definisikan matriks A, C, dan D, serta E
A = np.array([[3, 0], [-1, 2], [1, 1]])
C = np.array([[1, 4, 2], [3, 1, 5]])
D = np.array([[1, 5, 2], [-1, 0, 1], [3, 2, 4]])
E = np.array([[6, 1, 3], [-1, 1, 2], [4, 1, 3]])

# Perkalian A * C
AC = np.dot(A, C)

# Penjumlahan D + E
D_plus_E = D + E

# Pengurangan D - E
D_minus_E = D - E

# Menampilkan hasil
print("Hasil A * C:")
print(AC)
print("\nHasil D + E:")
print(D_plus_E)
print("\nHasil D - E:")
print(D_minus_E)
