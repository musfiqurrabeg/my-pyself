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


