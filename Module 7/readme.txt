Name: Nathalie Agustin - nagusti1
Module 7: Frequency Analysis	Due: March 13, 2022 11:59 PM

Approach:
1. Open the files and set up the needed dictionaries for comparison. The required dictionares are one for the ciphertext character frequencies which is generated from get_freq_counts(ciphert_text), and another one from the given text file freq.txt.
2. get_freq_counts adds entries to a dictionary based on the provided ciphertext. Characters from the ciphertext string become the keys, and the number of occurrences become the values for those keys. 
3. The dictionary is sorted by most frequently occurring to least frequently occurring characters to match the provided freq.txt format.
4. The freq.txt file is re-formatted to a dictionary by splitting the key-values at the ":".  These key-value pairs are added as entries to the new dictionary, plain_freq. 
5. A final dictionary is created named decrypt_key. The cipher_freq dictionary keys become the keys of decrypt_key. The plain_freq freq.txt dictionary keys become the values of decrypt_key. 
6. In the decrypt function, decrypt_key dictionary becomes the lookup table for what the ciphertext characters should map to. Each character in the ciphertext a key to look up in the decrypt_key dictionary, and the value for that character is appended to a final string as the decrypted plaintext.
7. The final string is returned and printed. Both files are closed per best practice.

Sources: 
https://www.adamsmith.haus/python/answers/how-to-convert-a-file-into-a-dictionary-in-python
https://towardsdatascience.com/sorting-a-dictionary-in-python-4280451e1637

Known Bugs:
The decryption function will only have a 95% accuracy because of characters that occur with the same frequency. If they have the same frequency, there is a chance that the wrong characters will be mapped to each other. This was the case with "l" and "m" in our decrypted message. 

-----------------------------------------------------------------

Hand-Decrypted Secret Message:
ltcol thorn are the oss agents meeting in the rear of saint marys south church after rear admiral smith returns from his travel abroad to mauritania for operation illicitscent