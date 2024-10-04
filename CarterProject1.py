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

    return output

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

    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    # Convert the key to itself but lowercase (.loewr)
    key = key.lower()

    # create new temp key which is the input key text replacing all of the words
    # in the plaintext ignore if it is not in the alphabet and ignore if it is a space
    # still add them to the new string however
    stringReplacedPlainTextOfKey = ''
    indexOfKey = 0
    for i in plaintext:
        # https://www.toppr.com/guides/python-guide/references/methods-and-functions/methods/string/isalpha/python-string-isalpha/#:~:text=To%20check%20if%20all%20the,If%20not%2C%20it%20returns%20False.
        if i.isalpha():
            stringReplacedPlainTextOfKey += key[indexOfKey % len(key)]
            indexOfKey += 1
        else:
            stringReplacedPlainTextOfKey += i

    # Create temp var for the output
    output = ''

    # Iterate thru all of the chars
    # if it is uppercase then bump the key and then add on the new letter
    # make sure it is modded the value of the alphabet length
    # then append it onto the temo output var
    for i, char in enumerate(plaintext):
        # If it is not upper or lower (meaning it is special char or space)
        # then simply output that into the temp var.
        if not char.isalpha():
            output += char
        # Find the upper value with the offeset in mind
        if char.isupper():
            offsetValueOfIndex = alphabet.upper().index(stringReplacedPlainTextOfKey[i].upper())
            output += alphabet.upper()[(alphabet.upper().index(char) + offsetValueOfIndex) % len(alphabet)]
        # if it is  lowercase then shift up again on the upper alphabet
        # then the new letter same condition
        # then append that char onto the temp output var
        elif char.islower():
            offsetValueOfIndex = alphabet.index(stringReplacedPlainTextOfKey[i].lower())
            output += alphabet[(alphabet.index(char) + offsetValueOfIndex) % len(alphabet)]

    # Print the output var
    return output

def keywordDecrypt(key, encryptedValue):

    # Remove all of the duplicates from the key while keeping them sorted
    # Add an indexer value if needed
    key = "".join(sorted(set(key), key=key.index)).upper()

    # Copy alpha var
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    # create dups alphabet with key shifted with no Dups
    firstComeFirstServeAlphabet = key + "".join([char for char in alphabet if char not in key])

    # mashmap the subs and substitue the alpha to normal alphabet
    cryptedHashAlpha = {modifiedChar: normalAlphaChar for modifiedChar, normalAlphaChar in zip(firstComeFirstServeAlphabet, alphabet)}

    # temp decrypt var
    output = ""

    # Iterate thru string of input text
    for char in encryptedValue:
        if char.upper() in cryptedHashAlpha:
            decrypted_char = cryptedHashAlpha[char.upper()]
            if char.isupper():
                # if is upper then set the new char to it in string but uppercase
                output += decrypted_char.upper()
            else:
                # if it is lower then set the new char to output but lower to preserver case
                output += decrypted_char.lower()
        else:
            # append any non alpha char to the output
            output += char

    # return the output
    return output

def columnarDecrypt(key, encryptedValue):
    print("Columnar Decryptor")

def vigenereDecrypt(key, encryptedValue):

    # copy alpha var

    # Take keyboard input and standardize the key to lowercase

    # iterate over the encrypted value to learn where special non-alpha chars are
    # Store it with an index of the value key to ensure that the key is repeated over the value of text.

    # create temp output var

    # iterate thru encryptedValue with counter

    # if it is non alpha immediately append to output

    # check state and ensure is upper and lower is in place

    # keep in mind the shift and append it to the output (one for upper and one for lower)

    # return output
    print("OUTPUT")

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
    return cipherFunctions[cipherMethod][cipherAction](key, text)

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

            print(startAction(cipherMethod, cipherAction, key, text))
