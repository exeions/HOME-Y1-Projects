alphabet = "abcdefghijklmnopqrstuvwxyz"
ALPH = alphabet.upper()

def Main():
    print("--------------Welcome to the Caesar Cipher of the Century!--------------")
    input("Press any button to continue ")
    
    options = "---Options---\n" \
    "1. Encrypt Message\n2. Decrypt Message\n3. Exit"
    print(options)
    
    while True:
        selection = input(": ")

        if selection == "1":
            
            print("Encryption Selected!")
            
            txt = input("Input text: ")
            num = input("Input shift: ")

            try:
                shift = int(num)
                encrypt(txt, shift)
            except ValueError:
                print("Invalid shift.")
            break
        
        elif selection == "2":

            print("Decryption Selected!")

            txt = input("Input text: ")
            num = input("Input shift: ")
            
            try:
                shift = int(num)
                decrypt(txt, shift)
            except ValueError:
                print("Invalid shift.")
            break

        elif selection == "3":
            print("Exitting Caesar Cipher.")
            break

        else:
            print("Invalid option! Please try again.")

def encrypt(message, shift):

    encrypted = ""

    for char in message:
        if char in ALPH:
            index = ALPH.index(char) ## Current character index
            new_index = (index + shift) % len(ALPH)
            encrypted += ALPH[new_index]
        elif char in alphabet:
            index = alphabet.index(char) ## Current character index
            new_index = (index + shift) % len(alphabet)
            encrypted += alphabet[new_index]
        else:
            encrypted += char

    print("Encrypted:", encrypted)


def decrypt(message, shift):
    
    decrypted = ""

    for char in message:
        if char in ALPH:
            index = ALPH.index(char) ## Current character index
            new_index = (index - shift) % len(ALPH)
            decrypted += ALPH[new_index]
        elif char in alphabet:
            index = alphabet.index(char) ## Current character index
            new_index = (index - shift) % len(alphabet)
            decrypted += alphabet[new_index]
        else:
            decrypted += char
    
    print("Decrypted:", decrypted)

Main()