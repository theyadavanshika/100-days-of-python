alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(original_text, shift_amount): 
    cipher_text = ""
    for letter in original_text:
        shifted_position = (alphabet.index(letter) + shift_amount) 

        shifted_position = shifted_position % len(alphabet) #(0 -> 25) range 
        cipher_text += alphabet[shifted_position] 

    print(f"Here's the encoded result : {cipher_text}")

def decrypt(original_text, shifted_amount):
    cipher_dtext = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) - shifted_amount
        shifted_position = ((shifted_position % len(alphabet)) + len(alphabet)) % len(alphabet)
        cipher_dtext += alphabet[shifted_position] 

    print(f"Here's the decoded result : {cipher_dtext}") 

def caesor(direction, text, shift):
    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)

caesor(direction=direction, text=text, shift=shift)