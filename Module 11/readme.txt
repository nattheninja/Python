Name: Nathalie Agustin - nagusti1
Module 10: Hill Cipher	Due: April 18, 2022 11:59 PM

Approach:
- Created function to calculate determinant in accordance with assignment formula
- Created function to verify if the given key matrix is invertible if the determinant = 0
- Created mod_inverse(). A while loop that runs until the determinant multiplied by some value % 26 = 1. That value is the modular multiplicative inverse.
- Created helper function called encoding() to create a dictionary that will map the letters to the assignment-specified numbers. 
- Created function encrypt() that first converts the given plaintext into numbers. The numbers are reformatted into 2x1 NumPy arrays and placed in a list. Once formatted into an array, the modular matrix multiplication is performed between the plaintext columns and the given key which results in the encrypted values. The values are then mapped back to their alphabet counterpart, and the results are printed and returned.
- Created helper function format_inverse() that rearranges the key matrix in preparation for calculating the matrix inverse. In a 2x2 matrix, the values for a and d are switched, and the values for b and c are negated. Returns re-formatted matrix.
- Created decrypt() function that leverages format-inverse() to create the inverse matrix of the given key. Matrix multiplication is then performed by the inverted key matrix and each ciphertext column. The integers are converted back to the alphabet character and the results are printed. 
- In main(), the different keys are defined. A for loop is created to try each of the given keys. A try:/except: statement is used to handle errors if the matrix is not the right shapre or if the matrix is not invertible. All results are printed. 

Known Bugs:
- This version is coded only for the use of modulus of 26. If we want to accomodate alternative modulus values, we would simply add a parameter in the functions for a generic modulus variable.
- Creating a custom MatrixNotInvertible Exception class and raising it will halt program execution at the first exception found. In order to continue multiple Hill Cipher attempts, only string errors are given. 

