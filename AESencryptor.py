from Crypto.Cipher import PKCS1_OAEP,AES
from Crypto.Random import get_random_bytes
import os

def encrypt_message(file_path, public_key):
    aes_key = get_random_bytes(32)
    aes_cipher = AES.new(aes_key, AES.MODE_GCM)

    cipher = PKCS1_OAEP.new(public_key)

    with open(file_path, "rb") as f:
        message = f.read()

    cipherText, tag = aes_cipher.encrypt_and_digest(message)   

    rsa_cipher = PKCS1_OAEP.new(public_key)
    encrypted_aes_key = rsa_cipher.encrypt(aes_key) 

    try:
        with open("encrypted_file.txt", "wb") as f:
            for enryptedText in (encrypted_aes_key, aes_cipher.nonce, tag, cipherText):
                f.write(enryptedText)
        print("NEW AES-ENCRYPTED FILE CREATED")
    except:
        print("An Error occurred while encryption.")    