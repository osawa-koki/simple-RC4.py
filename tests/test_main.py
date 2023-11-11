import pytest

from app.rc4 import decrypt, encrypt


@pytest.mark.parametrize(
    "key, message",
    [
        ("key", "message"),
        ("hogehoge", "fugafuga"),
        ("あいうえお", "かきくけこ"),
        ("🐙🐬🐸", "🦈🦀🐳🦑🦪"),
    ],
)
def test_add(key, message):
    encrypted = encrypt(message, key)
    decrypted = decrypt(encrypted, key)
    assert message == decrypted
