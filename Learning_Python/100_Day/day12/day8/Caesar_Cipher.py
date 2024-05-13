# Resource
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

from caesar_art import logo

print(logo)

"""
# The encryption function
def encrypt (input_text, shift_number):
    cipher_text = []
    for letter in input_text:
        position = alphabet.index(letter)
        cipher_index = position + shift_number
        
        cipher_text += alphabet[cipher_index]
        
    print(f"The encoded text is {''.join(cipher_text)}")
        
# The decryption function
def decrypt(input_text, shift_number):
    decoded_text = []
    for letter in input_text:
        position = alphabet.index(letter)
        decoded_index = position - shift_number
        
        decoded_text += alphabet[decoded_index]
        
    print(f"The decoded text is {''.join(decoded_text)}")
"""
restart_program = True

while not restart_program == False:

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Join the encrypt and decrypt funtion together
    def ceaser(input_text, shift_number, the_direction):
        ceaser_text = []
        for char in input_text:
            if char in alphabet:
                position = alphabet.index(char)
                if the_direction == "encode":
                    ceaser_index = position + shift_number
                elif the_direction == "decode":
                    ceaser_index = position - shift_number
                
                ceaser_text += alphabet[ceaser_index]
            else:
                ceaser_text += char
            
        print(f"The {the_direction} text is {''.join(ceaser_text)}")


    # What if the user input shit greater than the len aplphabet?
    shift = shift % 26
    print(shift)

    # Call the ceaser function
    ceaser(text, shift, direction)
    
    input_restart = input("Are you want to restart the program? yes or no? : ")
    input_restart = input_restart.lower()
    
    if input_restart == "no":
        restart_program = False



