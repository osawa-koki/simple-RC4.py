import base64


def ksa(key: bytes) -> list[int]:
    s = list(range(256))
    j = 0
    for i in range(256):
        j = (j + s[i] + key[i % len(key)]) % 256
        s[i], s[j] = s[j], s[i]
    return s


def prga(s: list[int]) -> list[int]:
    k = [0] * 256
    i = 0
    j = 0
    for idx in range(256):
        i = (i + 1) % 256
        j = (j + s[i]) % 256
        s[i], s[j] = s[j], s[i]
        k[idx] = s[(s[i] + s[j]) % 256]
    return k


def encrypt(data: str, key: str) -> str:
    _data = data.encode()
    _key = key.encode()
    s = ksa(_key)
    gen = prga(s)
    result = bytes([_data[i] ^ gen[i] for i in range(len(_data))])
    return base64.b64encode(bytes(result)).decode()


def decrypt(data: str, key: str) -> str:
    _data = base64.b64decode(data)
    _key = key.encode()
    s = ksa(_key)
    gen = prga(s)
    result = bytes([_data[i] ^ gen[i] for i in range(len(_data))])
    return result.decode()
