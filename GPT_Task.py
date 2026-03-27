alphabet = "abcdefghijklmnopqrstuvwxyz"
ALPHA = alphabet.upper()

txt = input("Input text: ")
shift = int(input("Input shift: "))

def encrypt(message, key):

    encrypted = ""

    for char in  message:
        if char in alphabet:
            old_index = alphabet.index(char)
            new_index = (old_index + key) % len(alphabet)
            encrypted += alphabet[new_index]
        
        elif char in ALPHA:
            old_index = ALPHA.index(char)
            new_index = (old_index + key) % len(ALPHA)
            encrypted += ALPHA[new_index]
        
        else:
            encrypted += char


    print(encrypted)

encrypt(txt, shift)