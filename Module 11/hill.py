import numpy as np


# Accepts a matrix, calculates and returns determinant
def determinant(matrix):
    return (matrix[0, 0] * matrix[1, 1]) - (matrix[0, 1] * matrix[1, 0])


# returns True if the matrix is invertible and False otherwise
def invertible(matrix):
    if determinant(matrix) != 0:
        return True
    else:
        return False


def mod_inverse(det, m):
    """Accepts a number determinant and a modulus m
     Returns the modular multiplicative inverse of n modulo m"""
    inverse = 0
    det = det % m
    while (det * inverse) % m != 1:
        inverse += 1
    return inverse


def encoding():
    """ Creates lookup table """
    scheme = {}
    i = 0
    from string import ascii_uppercase
    for letter in ascii_uppercase:
        scheme[letter] = i
        i += 1
    return scheme


def encrypt(key, ptext):
    scheme = encoding()
    text = []
    text_matrix = []
    encrypted = []
    cipher_array = []

    # Encode plaintext to numbers
    for char in ptext:
        text.append(np.array([scheme.get(char)]))

    # Reformat matrix to 2 x 1 arrays (row x col)
    plain_matrix = np.array(text)
    plain_matrix.resize(int(len(ptext) / 2), 2)
    for i in range(int(len(ptext) / 2)):
        temp = plain_matrix[i]
        temp.resize(2, 1)
        text_matrix.append(temp)
    # Matrix multiplication of plaintext columns and key
    for column in text_matrix:
        encrypted.append((key @ column % 26).astype(int))
    # Convert integers back to alphabet encoding scheme
    for item in encrypted:
        for num in item:
            for key, value in scheme.items():
                if value == int(num):
                    cipher_array.append(key)

    print(f"Plaintext: {ptext}")
    print(f"Plaintext column vectors: {text_matrix}")
    print()
    print("Ciphertext: " + "".join(cipher_array))
    print(f"Ciphertext column vectors: {encrypted}")
    print()
    return encrypted


def format_inverse(key):
    """ In a 2x2 matrix, switches a & d, and sets b & c negative"""
    temp_a = key[0, 0]
    temp_d = key[1, 1]
    key[0, 0] = temp_d
    key[1, 1] = temp_a
    key[0, 1] = -key[0, 1]
    key[1, 0] = -key[1, 0]
    return key


def decrypt(cipher_matrix, key):
    """Calculates the modular multiplicative inverse of the determinant of K
    and multiplies the scalar result by the key matrix
    """
    scheme = encoding()
    det = determinant(key)
    mult_inverse = mod_inverse(det, 26)
    # Creates modular inverse matrix of the given key
    key_inverse = (mult_inverse * format_inverse(key)) % 26
    decrypted = []
    decrypted_list = []
    # Matrix multiplication of cipher columns and key_inverse
    for columns in cipher_matrix:
        decrypted.append((key_inverse @ columns % 26).astype(int))
    # Convert integers back to alphabet encoding scheme
    for item in decrypted:
        for num in item:
            for key, value in scheme.items():
                if value == int(num):
                    decrypted_list.append(key)
    print("Plaintext: " + "".join(decrypted_list))
    print(f"Plaintext column vectors: {decrypted}")


def main():
    key1 = np.array([[19, 8, 4], [3, 12, 7]])
    key2 = np.array([[7, 8], [11, 11]])
    key3 = np.array([[5, 15], [4, 12]])
    keys = [key1, key2, key3]

    for key in keys:
        print("Attempting hill cipher...")
        if not invertible(key):
            print("-------------------------------")
            print(f"The determinant of the key = 0")
            print("-------------------------------")
            break
        try:
            decrypt(encrypt(key, "ATTACKATDAWN"), key)
        except:
            print("-----------------------------")
            print("The matrix is not a square. ")
            print("-----------------------------")
        finally:
            print()


if __name__ == "__main__":
    main()
