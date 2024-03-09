def encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shifted = ord(char) + shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def decrypt(text, shift):
    return encrypt(text, -shift)

def main():
    choice = input("Enter 'e' for encryption or 'd' for decryption: ").lower()
    if choice not in ['e', 'd']:
        print("Invalid choice.")
        return

    text = input("Enter the message: ")
    shift = int(input("Enter the shift value: "))

    if choice == 'e':
        encrypted_text = encrypt(text, shift)
        print("Encrypted message:", encrypted_text)
    else:
        decrypted_text = decrypt(text, shift)
        print("Decrypted message:", decrypted_text)

if __name__ == "__main__":
    main()
