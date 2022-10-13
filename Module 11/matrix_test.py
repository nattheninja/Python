import numpy as np

def mod_inverse(det, m):
    """Accepts a number determinant and a modulus m
     Returns the modular multiplicative inverse of n modulo m"""
    inverse = 0
    det = det % m
    while (det * inverse) % m != 1:
        inverse += 1
    return inverse


k = np.array([[3, 3], [2, 5]])

print(k)

temp_a = k[0, 0]
temp_d = k[1, 1]
k[0, 0] = temp_d
k[1, 1] = temp_a
k[0, 1] = -k[0, 1]
k[1, 0] = -k[1, 0]

determinant = np.linalg.det(k)
print(int(determinant))
# print(mod_inverse(determinant, 26))
print((3*k) % 26)

key2 = np.array([[7, 8], [11, 11]])
print(np.linalg.det(key2))
