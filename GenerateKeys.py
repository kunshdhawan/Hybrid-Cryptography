from Crypto.PublicKey import RSA
import os

def generate_rsa_keys():
    if not os.path.exists("private_rsa_key.pem") or not os.path.exists("public_rsa_key.pem"):
        keys = RSA.generate(2048)
        private_rsa_key = keys
        public_rsa_key = keys.public_key()

        with open("private_rsa_key.pem", "wb") as f:
            f.write(private_rsa_key.export_key())
            print("RSA PRIVATE KEY GENERATED")

        with open("public_rsa_key.pem", "wb") as f:
            f.write(public_rsa_key.export_key())
            print("RSA PUBLIC KEY GENERATED")
    else:
        print("PREVIOUS RSA FOUND.")
