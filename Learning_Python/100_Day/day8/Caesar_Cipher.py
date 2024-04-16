alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# The encryption function
def encrypt (input_text, shift_number):
    cipher_text = []
    for letter in input_text:
        position = alphabet.index(letter)
        cipher_index = position + shift_number
        
        cipher_text += alphabet[cipher_index]
        
    print(f"{''.join(cipher_text)}")
        
# The decryption function
def decrypt(input_text, shift_number):
    decoded_text = []
    for letter in input_text:
        position = alphabet.index(letter)
        decoded_index = position - shift_number
        
        decoded_text += alphabet[decoded_index]
        
    print(f"{''.join(decoded_text)}")

# Call the encrypt function
encrypt(text, shift)

# Call the decrypt function
decrypt(text, shift)





