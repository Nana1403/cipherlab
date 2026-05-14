from itertools import cycle

def vigenere(text, key, mode='encrypt'):
    text = text.upper()
    key = key.upper()
    
    # Filter key to include only alphabetic characters
    key_chars = [c for c in key if c.isalpha()]
    key_cycle = cycle(key_chars)
    
    result = []
    for char in text:
        if char.isalpha():
            # Find the shift value (A=0, B=1, ..., Z=25)
            shift = ord(next(key_cycle)) - ord('A')
            
            # Apply shift: + for encryption, - for decryption
            if mode == 'decrypt':
                shift = -shift
            # Perform rotation mod 26
            new_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
            result.append(new_char)
        else:
            result.append(char)
            
    return "".join(result)

# # Test-----
# msg = "La La Land"
# secret_key = "SINGER"

# encrypted = vigenere(msg, secret_key, 'encrypt')
# print(f"Encrypted: {encrypted}") # Output: RIJVS UYVJN!

# decrypted = vigenere(encrypted, secret_key, 'decrypt')
# print(f"Decrypted: {decrypted}") # Output: HELLO WORLD!
