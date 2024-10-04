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

    # Remove the spaces from the input text

    # Calculate the number of rows that are required according to the formula

    # Create 2 d array grid

    # Sort the values of the key alphabetically

    # Reorder all of the columns based on the alpha order of the key itself.

    # Read the Grid Column-by-Column

    # Create output string

    # Iterate over the columsn and rows to read the output line by line and store in text output string.

    # Print the output
    print("EXIT")


def vigenere(key, plaintext):

    # Create the alphabet again. (Uppercase)
    # Create the alphabet but only lower .upper; .lower

    # Convert the key to itself but lowercase (.loewr)

    # create new temp key which is the input key text replacing all of the words
    # in the plaintext ignore if it is not in the alphabet and ignore if it is a space
    # still add them to the new string however

    # Create temp var for the output

    # Iterate thru all of the chars
    # if it is uppercase then bump the key and then add on the new letter make sure it is modded the value of the alphabet length
    # then append it onto the temo output var

    # if it is  lowercase then shift up again on the upper alphabet
    # then the new letter same condition
    # then append that char onto the temp output var

    # If it is neither uppercase or lowercase (meaning it is special char or space)
    # then simply output that into the temp var.

    # Print the output var

    print("EXIT")

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
