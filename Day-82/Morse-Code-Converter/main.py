from morse_dictionary import morse_code

while True:
    text = input("Enter text to convert (or type 'quit' to exit): ").upper()

    if text == "EXIT123":
        print("Goodbye!")
        break

    if not text:
        print("Please enter some text.")
        continue

    result = []

    for char in text:
        coded_text = morse_code.get(char, "?")
        result.append(coded_text)

    print("Morse code:", " ".join(result))
