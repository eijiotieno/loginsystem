from cryptography.fernet import Fernet

class Encrypt(object):
    def __init__(self, file):
        self.file = file
        self.key = self.key_reader()

    def key_reader(self):
        with open("keyfile.text", "rb") as filekey:
            key = filekey.read()
        return key

    def key_generator(self):
        key = Fernet.generate_key()
        with open("keyfile.text", "wb") as filekey:
            filekey.write(key)

    def encryption(self):
        with open("keyfile.text", "rb") as filekey:
            key = filekey.read()

        fernet = Fernet(self.key)
        with open(self.file, "rb") as file:
            original = file.read()

        encrypted = fernet.encrypt(original)
        with open(self.file, "wb") as encrypted_file:
            encrypted_file.write(encrypted)

    def decryption(self):
        fernet = Fernet(self.key)
        with open(self.file, "rb") as enc_file:
            encrypted = enc_file.read()

        decrypted = fernet.decrypt(encrypted)
        with open(self.file, "wb") as dec_file:
            dec_file.write(decrypted)
