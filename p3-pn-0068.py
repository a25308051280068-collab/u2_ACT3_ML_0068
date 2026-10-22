import numpy as np

# ==========================================
# 1. Estadística Básica en Arreglos NumPy
# ==========================================

n0068 = np.array([12, 45, 67, 23, 89])
print(n0068)
print(n0068[0])
print(n0068[2])
# Se ajustan los índices 5 y 9 a posiciones válidas dentro de los 5 elementos (0 al 4)
print(n0068[3]) 
print(n0068[4])
print("-----------------------------------------------------")

# Matriz 2D (2 filas x 3 columnas)
n0068 = np.array([
    [10, 20, 30],
    [45,  7,  3],
])
print(n0068)
print(n0068[0,0])
print(n0068[1,2])
print(n0068[-1,-2])
# Se ajusta el índice negativo -3 a -2 (la matriz solo tiene 2 filas)
print(n0068[-2,-1])

print("-----------------------------------------------------")

# Arreglo 3D (2 bloques x 2 filas x 3 columnas)
n0068 = np.array([
    [
        [10, 20, 30],
        [45,  7,  3]
    ],
    [
        [70, 80, 90],
        [100, 118, 120]
    ]
])

print(n0068)
print(n0068[0,0,0])
print(n0068[1,1,2])
print(n0068[-1,-1,-2])

print("Christian garcia jimenez nc0 0068")
