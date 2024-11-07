from Crypto.PublicKey import RSA

def load_rsa_keys():
    try:
        with open("private_rsa_key.pem", "rb") as f:
            private_rsa_key = RSA.import_key(f.read())
            print("RSA PRIVATE KEY LOADED")

        with open("public_rsa_key.pem", "rb") as f:
            public_rsa_key = RSA.import_key(f.read())
            print("RSA PUBLIC KEY LOADED")

        return private_rsa_key, public_rsa_key
    
    except (ValueError, IOError) as e:
        print(f"Error loading RSA keys: {e}")
        return None, None
