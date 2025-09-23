import os
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
from dotenv import load_dotenv
from typing import Union

load_dotenv()

BASE_PATH = os.getenv("BASE_PATH", os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
DEFAULT_IV_LENGTH = 16  # AES block size


def encrypt_cfb(plaintext: bytes, key: bytes, iv: bytes) -> bytes:
    """
    Encrypts the given plaintext using AES CFB mode.
    """
    if not isinstance(plaintext, bytes) or not isinstance(key, bytes) or not isinstance(iv, bytes):
        raise TypeError("All parameters must be bytes.")

    if len(iv) != DEFAULT_IV_LENGTH:
        raise ValueError(f"IV must be {DEFAULT_IV_LENGTH} bytes long.")

    try:
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(plaintext) + encryptor.finalize()
        print("✅ Encryption successful")
        return ciphertext
    except Exception as e:
        print(f"⚠️ Encryption failed: {str(e)}")
        raise


def decrypt_cfb(ciphertext: bytes, key: bytes, iv: bytes) -> bytes:
    """
    Decrypts the given ciphertext using AES CFB mode.
    """
    if not isinstance(ciphertext, bytes) or not isinstance(key, bytes) or not isinstance(iv, bytes):
        raise TypeError("All parameters must be bytes.")

    if len(iv) != DEFAULT_IV_LENGTH:
        raise ValueError(f"IV must be {DEFAULT_IV_LENGTH} bytes long.")

    try:
        cipher = Cipher(algorithms.AES(key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        plaintext = decryptor.update(ciphertext) + decryptor.finalize()
        print("✅ Decryption successful")
        return plaintext
    except Exception as e:
        print(f"⚠️ Decryption failed: {str(e)}")
        raise


def check_base_path():
    if not os.path.exists(BASE_PATH):
        raise FileNotFoundError(f"⚠️ BASE_PATH not found: {BASE_PATH}")
    print(f"✅ BASE_PATH verified: {BASE_PATH}")


def main():
    check_base_path()

    key = b"Sixteen byte key"  # 16 bytes key for AES-128
    iv = b"InitializationVe"   # 16 bytes IV
    plaintext = b"This is a test message."

    try:
        encrypted = encrypt_cfb(plaintext, key, iv)
        decrypted = decrypt_cfb(encrypted, key, iv)

        print("Encrypted:", encrypted)
        print("Decrypted:", decrypted)

        assert plaintext == decrypted, "⚠️ Decryption mismatch!"
        print("✅ Encryption/Decryption round-trip successful")
    except Exception as e:
        print(f"⚠️ Main process error: {e}")


if __name__ == "__main__":
    main()
