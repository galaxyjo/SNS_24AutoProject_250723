import pytest
from modules.common import _mode_cfb_61b4dddb as cfb


@pytest.fixture
def sample_data():
    return {
        "key": b"Sixteen byte key",
        "iv": b"InitializationVe",
        "plaintext": b"This is a test message.",
        "empty": b"",
    }


def test_encrypt_decrypt_cfb(sample_data):
    ciphertext = cfb.encrypt_cfb(sample_data["plaintext"], sample_data["key"], sample_data["iv"])
    decrypted = cfb.decrypt_cfb(ciphertext, sample_data["key"], sample_data["iv"])
    assert decrypted == sample_data["plaintext"]


def test_encrypt_decrypt_empty_input(sample_data):
    ciphertext = cfb.encrypt_cfb(sample_data["empty"], sample_data["key"], sample_data["iv"])
    decrypted = cfb.decrypt_cfb(ciphertext, sample_data["key"], sample_data["iv"])
    assert decrypted == sample_data["empty"]


@pytest.mark.parametrize("pt, key, iv", [
    ("not-bytes", b"validkey12345678", b"validIV123456789"),
    (b"bytes", "not-bytes", b"validIV123456789"),
    (b"bytes", b"validkey12345678", "not-bytes"),
])
def test_encrypt_cfb_type_error(pt, key, iv):
    with pytest.raises(TypeError):
        cfb.encrypt_cfb(pt, key, iv)


@pytest.mark.parametrize("ct, key, iv", [
    ("not-bytes", b"validkey12345678", b"validIV123456789"),
    (b"bytes", "not-bytes", b"validIV123456789"),
    (b"bytes", b"validkey12345678", "not-bytes"),
])
def test_decrypt_cfb_type_error(ct, key, iv):
    with pytest.raises(TypeError):
        cfb.decrypt_cfb(ct, key, iv)


def test_invalid_iv_length(sample_data):
    short_iv = b"short"
    with pytest.raises(ValueError):
        cfb.encrypt_cfb(sample_data["plaintext"], sample_data["key"], short_iv)
    with pytest.raises(ValueError):
        cfb.decrypt_cfb(b"dummydata", sample_data["key"], short_iv)
