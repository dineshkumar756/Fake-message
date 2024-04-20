# from Crypto.Cipher import AES
# from Crypto.Util.Padding import pad, unpad
# from Crypto.Random import get_random_bytes

# def encrypt_AES(key, plaintext):
#     cipher = AES.new(key, AES.MODE_CBC)
#     ciphertext_bytes = cipher.encrypt(pad(plaintext.encode('utf-8'), AES.block_size))
#     return ciphertext_bytes, cipher.iv

# def decrypt_AES(key, iv, ciphertext):
#     cipher = AES.new(key, AES.MODE_CBC, iv)
#     plaintext_bytes = unpad(cipher.decrypt(ciphertext), AES.block_size)
#     return plaintext_bytes.decode('utf-8')

# # Example usage
# key = get_random_bytes(16)  # 16 bytes key for AES-128
# plaintext = "Hello, this is a secret message!"

# # Encrypt
# ciphertext, iv = encrypt_AES(key, plaintext)
# print("Ciphertext:", ciphertext.hex())
# print("IV:", iv.hex())

# # Decrypt
# decrypted_text = decrypt_AES(key, iv, ciphertext)
# print("Decrypted text:", decrypted_text)




# import base64

# # Base64-encoded string
# encoded_string = 'aGVsbG8='

# # Convert base64-encoded string to binary
# binary_data = base64.b64decode(encoded_string)

# print("Decoded binary:", binary_data)

import sys
import base64
from Crypto.Cipher import AES


class AESCipher(object):
    def __init__(self, key):
        self.bs = 16
        self.cipher = AES.new(key, AES.MODE_ECB)

    def encrypt(self, raw):
        raw = self._pad(raw)
        encrypted = self.cipher.encrypt(raw)
        encoded = base64.b64encode(encrypted)
        return str(encoded, 'utf-8')

    def decrypt(self, raw):
        decoded = base64.b64decode(raw)
        decrypted = self.cipher.decrypt(decoded)
        return str(self._unpad(decrypted), 'utf-8')

    def _pad(self, s):
        return s + (self.bs - len(s) % self.bs) * chr(self.bs - len(s) % self.bs)

    def _unpad(self, s):
        return s[:-ord(s[len(s)-1:])]