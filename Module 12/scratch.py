import numpy as np

matrix = np.array([[1, 1], [1, -1]]) / (2 ** (1 / 2))
pauli = np.array([[0, 1], [1, 0]])
test = np.array([[1], [0]])
print(pauli @ test)
print(pauli @ (pauli @ test))
