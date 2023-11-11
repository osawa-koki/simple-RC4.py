from rc4 import decrypt, encrypt

key = "key"
message = "message"

encrypted = encrypt(message, key)

print(encrypted)

decrypted = decrypt(encrypted, key)

print(decrypted)
