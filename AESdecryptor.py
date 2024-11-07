from Crypto.Cipher import PKCS1_OAEP,AES
import os

def decrypt_message(file_path, private_key):

    try:
        with open(file_path, "rb") as f:
            encrypted_aes_key = f.read(256)
            nonce = f.read(16)
            tag = f.read(16)
            cipherText = f.read()
    except:
        print("An Error occured while parsing the file.")    

    rsa_cipher = PKCS1_OAEP.new(private_key)
    aes_key = rsa_cipher.decrypt(encrypted_aes_key)

    aes_cipher = AES.new(aes_key, AES.MODE_GCM, nonce=nonce)
    decryptedText = aes_cipher.decrypt_and_verify(cipherText, tag) 

    try:
        with open("decrypted_file.txt", "wb") as f:
            f.write(decryptedText)
        print("NEW AES-DECRYPTED FILE CREATED")
    except:
        print("An Error occured while decryption.")

    print("Would like to destroy the current Public & Private Keys.")
    key_destroy = str(input("Choosing 'y' would require you to re-encrypt the file with a new pair of Public and Private Keys. y/n: "))

    if key_destroy.lower() == "y":
        os.remove("private_rsa_key.pem")
        os.remove("public_rsa_key.pem")
        print("BOTH PUBLIC AND PRIVATE RSA ARE DESTROYED")