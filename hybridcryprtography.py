import GenerateKeys, LoadKeys, AESencryptor, AESdecryptor

class HybridCryprtography:
    def __init__(self):
        GenerateKeys.generate_rsa_keys()
        self.private_key, self.public_key = LoadKeys.load_rsa_keys()

    def main(self):
        print("Choose an option")
        option = int(input("Encrypt:1 :: Decrypt:2 :: "))

        if option == 1:
            file_path = str(input("Enter the location of file to be encrypted.\n"))
            AESencryptor.encrypt_message(file_path, self.public_key)  

            also_decrypt = input("Would you also like to decrypt the encrypted file: y/n: ")
            if also_decrypt.lower() == "y":
                file_path = str(input("Enter the location of file to be decrypted.\n"))
                AESdecryptor.decrypt_message(file_path, self.private_key)
        elif option == 2:
            file_path = str(input("Enter the location of file to be decrypted.\n"))
            AESdecryptor.decrypt_message(file_path, self.private_key)     
        else:
            print("INVALID OPTION")    



if __name__ == "__main__":
    crypto = HybridCryprtography()
    crypto.main()    