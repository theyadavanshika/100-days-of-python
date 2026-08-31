from art import logo
print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(original_text, shifted_amount, encode_decode):
    cipher_text = ""

    if encode_decode == "decode":
        shifted_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            cipher_text += letter   
        elif letter in original_text:
            shifted_position = alphabet.index(letter) + shifted_amount
            shifted_position = ((shifted_position % len(alphabet)) + len(alphabet)) % len(alphabet)
            cipher_text += alphabet[shifted_position] 

    print(f"Here's the decoded result : {cipher_text}") 

while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(encode_decode = direction, original_text= text, shifted_amount= shift)

    restart = input("Type 'yes' if you want to go again, otherwise 'no'").lower()
    if restart != "yes":
        print("Thankyou\nGoodBye!!")
        break
    
    
        

    