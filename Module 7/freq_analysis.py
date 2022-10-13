def get_freq_counts(encrypted_msg):
    """Build dictionary, cipher characters are keys, frequency are values"""
    frequency = {}
    for char in encrypted_msg:
        if char not in frequency:
            frequency.setdefault(char, 1)
        else:
            # Increment frequency by one everytime char is seen
            frequency[char] = frequency.get(char) + 1
    # Sort dictionary by most frequently occurring char to least occurring
    sort_freq = sorted(frequency.items(), key=lambda y: y[1], reverse=True)
    frequency = dict(sort_freq)
    return frequency


def decrypt(cipher, plain, ciphertext):
    """ Decrypt ciphertext file using frequency dictionary"""

    """
    Maps the cipher frequency dict keys to the plaintext frequency 
    dict keys in a new dictionary called decrypt_key.
    The key-value pairs in decrypt_key are used to substitute
    the ciphertext with the plaintext characters.
    
    This function will decrypt approximately 95% of the ciphertext.
    """
    value = list(plain.keys())
    decrypt_key = dict.fromkeys(cipher)
    i = 0
    # Iterate over list of values and add as entries new dict
    for char in decrypt_key:
        decrypt_key[char] = value[i]
        i += 1
    # Build decrypted string from ciphertext
    plaintext = ""
    for char in ciphertext:
        plaintext += (decrypt_key.get(char))
    return plaintext


def main():
    # Build dictionary for frequency of ciphertext characters
    cipher_file = open("ciphertext.txt")
    cipher_text = cipher_file.read()
    cipher_freq = get_freq_counts(cipher_text)

    # Build dictionary for frequency of plaintext characters
    plain_freq = {}
    freq_file = open("freq.txt")
    for line in freq_file:
        # Separate keys from value from file line
        key, value = line.split(":")
        plain_freq[key] = int(value)

    # Final approximated plaintext
    print(decrypt(cipher_freq, plain_freq, cipher_text))
    cipher_file.close()
    freq_file.close()


if __name__ == "__main__":
    main()
