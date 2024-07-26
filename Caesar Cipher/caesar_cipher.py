# Way - 1
# from caesar_alphabet import alphabet
# from art import logo
# print(logo)
# should_end = False
# while not should_end:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n=>")
#     text = input("Type your message:\n=>").lower()
#     shift = int(input("Type the shift number:\n=>"))
#     shift = shift % 26
#     restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#     if restart == "no":
#         should_end = True
#         print("Good Bye!")
# Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# Inside the encrypt function, shift each letter of the text forwards in the alphabet by the shift amount and print the encrypted text
# def encrypt(plain_text , shift_amount):
#     cipher_text = ""
#     for letter in plain_text:
#         position = alphabet.index(letter)
#         new_position = position + shift_amount
#         new_letter = alphabet[new_position]
#         cipher_text += new_letter
#     print(f"The encoded text in {cipher_text}")
# Create a different function called 'decrypt' that takes the 'text' and 'shift' as inputs.
# Inside the 'decrypt' function, shift each letter of the 'text' *backwards* in the alphabet by the shift amount and print the decrypted text.
# def decrypt(cipher_text , shift_amount):
#     plain_text = ""
#     for letter in cipher_text:
#         position = alphabet.index(letter)
#         new_position = position - shift_amount
#         plain_text += alphabet[new_position]
#     print(f"The decoded text is {plain_text}")
# Check if the user wanted to encrypt or decrypt the message by checking the 'direction' variable. Then call the correct function based on that 'drection' variable.
# You should be able to test the code to encrypt *AND* decrypt a message.
# if direction == "encode":
#   encrypt(plain_text=text , shift_amount=shift)
# elif direction == "decode":
#     decrypt(plain_text=text , shift_amount=shift)
#
############################# Another Way ###########################:

# Combine the encrypt() and decrypt() functions into a single function called caesar().
from caesar_alphabet import alphabet
from art import logo
print(logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n=>")
    text = input("Type your message:\n=> ").lower()
    shift = int(input("Type the shift number:\n=> "))
    shift = shift % 26
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n=>")
    if restart == "no":
        should_end = True
        print("Good Bye!")

def caesar(start_text, shift_amount, cipher_direction):
    end_text = ""
    if cipher_direction == "decode":
        shift_amount *= -1
    for char in start_text:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift_amount
            end_text += alphabet[new_position]
        else:
            end_text += char
    print(f"Here's the {direction}d result: {end_text}")
# Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
caesar(start_text=text, shift_amount=shift, cipher_direction=direction)




# should_end = False
# while not should_end:
#     direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
#     text = input("Type your message:\n").lower()
#     shift = int(input("Type the shift number:\n"))
#     shift = shift % 26
# #Call the caesar() function, passing over the 'text', 'shift' and 'direction' values.
#     caesar(start_text=text , shift_amount=shift , cipher_direction=direction)
#     restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
#     if restart == "no":
#         should_end = True
#         print("Good Bye!")