from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

def encrypt(text, key_size):
    #generate key
    key = get_random_bytes(key_size) 
    cipher = AES.new(key, AES.MODE_EAX)

    #Convert text to bytes 
    data = text.encode('utf-8') 

    #Encrypt
    ciphertext, tag = cipher.encrypt_and_digest(data)
    
    return f"key: {key}, \n nonce: {cipher.nonce}, \n tag: {tag}, \nciphertext: {ciphertext}"

def decrypt(key, nonce, tag, ciphertext):
    cipher_dec = AES.new(key, AES.MODE_EAX, nonce=nonce)

    # Decrypt 
    plaintext = cipher_dec.decrypt_and_verify(ciphertext, tag)

    # Convert bytes back to a string
    return plaintext.decode('utf-8')

# # --- Test---
# key, nonce, tag, crypto_text = encrypt(" The secret message!", 16)
# print(decrypt(key, nonce, tag, crypto_text))
