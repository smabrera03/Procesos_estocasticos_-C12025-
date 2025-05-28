import numpy as np
import matplotlib.pyplot as plt
N = 200
U1 = np.random.uniform(low = 0, high = 2, size = N)
U2 = np.random.uniform(low = 0, high = 3, size = N)

U_vector = np.array([U1, U2])

#NOTA: fila 1 es U1, fila 2 es U2. Columna 1 es la primera realización de U_vector, 
# la segunda columna es la segunda realización de U_vector y así

col_0 = U_vector[: , 0]

print(U_vector[: , 0:3])
print("columan 1", col_0)
#que chiche python viejo. 

X1 = 0.5 * U1 - 0.3*U2
X2 = 0.7*U1 + 0.2*U2

X_vector = np.array([X1, X2])

print(U_vector[: , 0:3])
print(X_vector[: , 0:3])