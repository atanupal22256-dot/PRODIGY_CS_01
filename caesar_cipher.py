def caesar_cipher(text, shift, mode):
    result = ""
    
    # Adjust shift for decryption
    if mode == 'decrypt':
        shift = -shift
    
    for char in text:
        if char.isalpha():
            # Handle uppercase and lowercase separately
            start = ord('A') if char.isupper() else ord('a')
            # Perform the shift and stay within alphabet bounds
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            # Keep numbers and symbols as they are
            result += char
            
    return result

def main():
    print("--- Prodigy InfoTech: Cyber Security Project 1 ---")
    print("Caesar Cipher Tool")
    
    choice = input("Do you want to (encrypt/decrypt)? ").lower()
    message = input("Enter your message: ")
    shift = int(input("Enter the shift value (e.g., 1-25): "))
    
    output = caesar_cipher(message, shift, choice)
    print(f"\nResult: {output}")

if __name__ == "__main__":
    main()

