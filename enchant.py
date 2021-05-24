import re

def encrypt(message):
    
    patternForEncryption = re.compile("(?P<eins>.) (?P<zwei>.)")
    encryptedMessage = re.sub(patternForEncryption,"\g<eins>\g<zwei> ",message)
    print(encryptedMessage)

def decrypt(message):
    patternForDecryption = re.compile("(?P<eins>.)(?P<zwei>.) ")
    decryptedMessage = re.sub(patternForDecryption,"\g<eins> \g<zwei>",message)
    print(decryptedMessage)

print("Hello, what would you like to do?\n\nPress\n E for encryption\n D for decryption")

option = input()
if str(option) != "e" and str(option) != "d":
    print("sorry mate, press the right buttons please!")

if str(option) == "e":
    input_message = input("Please enter the message you want to encrypt:\n")
    encrypt(input_message)

if str(option) == "d":
    input_message = input("Please enter the message you want to decrypt:\n")
    decrypt(input_message)
