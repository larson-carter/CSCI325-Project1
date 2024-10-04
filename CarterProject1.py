def keyword(key, plaintext):

    # remove the dups from the key via hash
    # https://stackoverflow.com/questions/14538885/how-to-get-the-index-with-the-key-in-a-dictionary
    # Convert data to upper
    key = "".join(sorted(set(key), key=key.index)).upper()

    # create alphabet string var = "ABC..."
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # create a injected alphabet = "KEYWORD+ABC.... but remove the used chars from key"
    # NOTE: KEEP FIRST COME FIRST SERVER
    firstComeFirstServeAlphabet = key + "".join([char for char in alphabet if char not in key])

    # create empty output var
    output = ""

    # iterate thru the entire string
    for char in plaintext:
        #print(char)
        if char.upper() in alphabet:
            index = alphabet.index(char.upper())
            # append spliced char to output being uppercase if oriignal plain text slot is uppercase
            if char.isupper():
                output += firstComeFirstServeAlphabet[index].upper()
            else:
                # if it is not upper case then append regular, if it is not ASCII normal then append
                output += firstComeFirstServeAlphabet[index].lower()
        else:
            output += char

    # print the output
    print(output)

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

def takeKeywordInput():
    return input()

def takeInText():
    return input()

def startAction(cipherMethod, cipherAction, key, text):
    cipherFunctions = {
        "Keyword": {
            "Encrypt": keyword,
            "Decrypt": keywordDecrypt
        },
        "Columnar": {
            "Encrypt": columnar,
            "Decrypt": columnarDecrypt
        },
        "Vigenere": {
            "Encrypt": vigenere,
            "Decrypt": vigenereDecrypt
        }
    }
    cipherFunctions[cipherMethod][cipherAction](key, text)


if __name__ == '__main__':

    while True:
        exit = input("Press enter to continue or -1 to Exit\n")
        if exit == '-1':
            break
        else:
            print("Please select a cipher to apply:")

            cipherMethod = promptCipherToUse()

            print("Please select action:")

            cipherAction = promptAction()

            print("Please provide a keyword:")

            key = takeKeywordInput()

            print(f"Please provide a text to {cipherAction.lower()}:")

            text = takeInText()

            print(f"Starting {cipherMethod} Cipher.")

            print(text)

            startAction(cipherMethod, cipherAction, key, text)
