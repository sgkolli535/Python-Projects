# Sumedha Kolli
# This is part 2 of assignment 5, where the user's input is encrypted using the Caesar cipher method.
# the input of the user is stored in message.
message = input("Enter a message: ")
# the user's input is converted into all lower case letters to make sure it matches to the letters in the alphabet list.
message = message.lower()
# the message is converted into a list.
messageList = list(message)
# the shift for the decryption the user enters is converted into an integer.
shift = int(input("Enter a number to shift by (0-25): "))
# this is an empty list to store the resulting encrypted code.
enList = []
# this is an empty list to store the resulting decrypted code.
deList = []
# this is a list of all the letters in the alphabet to use for the encryption.
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v"
            , "w", "x", "y", "z"]
# this for loop is to encrypt the user's message.
# en is a variable that stands for each character in the "messageList".
for en in messageList:
    # if the character is a letter, then only is it considered to be part of the encryption process.
    if en.isalpha():
        # this for loop is finding every letter of the message within the alphabet list.
        for letterLocation in range(len(alphabet)):
            # this if loop is for if the letter in the message is found in the alphabet list.
            if en == alphabet[letterLocation]:
                # the "position" variable is shifting the original letter by the number of letters specified by user.
                # there is a "modulus 26" to allow for the shift to be looped from the end back to the beginning.
                position = (letterLocation + shift) % 26
                # the new encrypted letter is stored in the "newLetter" variable.
                newLetter = alphabet[position]
                # the new encrypted letter is added to "enList".
                enList.append(newLetter)
    # else statement is to keep all special characters, like spaces and punctuation, in the same position (not shifted).
    else:
        enList.append(en)
# these statements display the encrypted message.
print("Encrypting message.... ")
# the list of encrypted letters are joined back into a string.
encrypted = "".join(enList)
# "\t" is used to tab this statement after the previous one.
print("\tEncrypted message: ", encrypted)
# this for loop is to decrypt the encrypted message.
# de is a variable that stands for each character in enList.
for de in enList:
    # only the characters that are letters are decrypted.
    if de.isalpha():
        # the following code is similar to that of the encryption, with a few exceptions.
        for letterLocation in range(len(alphabet)):
            if de == alphabet[letterLocation]:
                # the shift is subtracted from the letterLocation to go back to the original letters.
                position = (letterLocation - shift) % 26
                # the new decrypted letter is stored as "oldLetter".
                oldLetter = alphabet[position]
                # the decrypted letter is added to "deList".
                deList.append(oldLetter)
    # else statement is to keep all special characters, like spaces and punctuation, in the same position (not shifted).
    else:
        deList.append(de)
# these statements display the decrypted message.
print("Decrypting message.... ")
# the list of the decrypted letters are joined back into a string.
decrypted = "".join(deList)
# the decrypted message and original message are printed with indents to compare that they are, in fact, the same.
print("\tDecrypted message: ", decrypted)
print("\tOriginal message: ", message)
