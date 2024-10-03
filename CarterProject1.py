def keyword(key, plaintext):
    print("Keyword Encryptor")

def columnar(key, plaintext):
    print("Columnar Encryptor")

def vigenere(key, plaintext):
    print("Vigenere Encryptor")

def keywordDecrypt(key, encryptedValue):
    print("Keyword Decryptor")

def columnarDecrypt(key, encryptedValue):
    print("Columnar Decryptor")

def vigenereDecrypt(key, encryptedValue):
    print("Vigenere Decryptor")

def promptCipherToUse():
    ciphers = ["Keyword", "Columnar", "Vigenere"]
    for i, cipher in enumerate(ciphers, 1):
        print(f"{i}.\t {cipher} Cipher")
    return ciphers[int(input())-1]

def promptAction():
    cipherOptions = ["Encrypt", "Decrypt"]
    for i, cipherOption in enumerate(cipherOptions, 1):
        print(f"{i}.\t {cipherOption}")
    return cipherOptions[int(input())-1]

if __name__ == '__main__':

    print("Please select a cipher to apply:")

    cipherMethod = promptCipherToUse()

    print("Please select action:")

    cipherAction = promptAction()

    print("Please provide a keyword:")

    # Take User Input here

    # make this encipher / decipher
    print("Please provide a text to encipher")

    # Take User Input HERE

    print("Starting SELECTED CIPHERE HERE Cipher")

    # Print the original message that they want to encipher

    # print the enciphereed text

    # loop until the user exits. i.e enter -1????


