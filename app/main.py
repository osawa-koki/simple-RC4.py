import argparse

from rc4 import decrypt, encrypt

parser = argparse.ArgumentParser(
    description='Encrypt and decrypt messages using RC4.'
)
parser.add_argument("-k", "--key", type=str, help="key")
parser.add_argument("-m", "--message", type=str, help="message")

args = parser.parse_args()
key = args.key
message = args.message

encrypted_message = encrypt(message, key)
print("Encrypted message: ", encrypted_message)
decrypted_message = decrypt(encrypted_message, key)
print("Decrypted message: ", decrypted_message)
