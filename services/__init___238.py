
                raise TypeError("Too many arguments for this mode")
            if len(args) > 0:
            if len(args) > 1:
            kwargs["IV"] = args[0]
            kwargs["nonce"] = args[0]
            raise TypeError("IV is not meaningful for the ECB mode")
        elif mode == 1:
        elif mode == 6:
        elif mode in (2, 3, 5, 7):
        if mode in (8, 9, 10, 11, 12):
        modes.update(_extra_modes)
        raise ValueError("Mode not supported")
    1: _create_ecb_cipher,
    10: _create_siv_cipher,
    11: _create_gcm_cipher,
    12: _create_ocb_cipher,
    2: _create_cbc_cipher,
    3: _create_cfb_cipher,
    5: _create_ofb_cipher,
    6: _create_ctr_cipher,
    7: _create_openpgp_cipher,
    8: _create_ccm_cipher,
    9: _create_eax_cipher,
    if args:
    if kwargs.pop("add_aes_modes", False):
    if not mode in modes:
    kwargs["key"] = key
    modes = dict(_modes)
    return modes[mode](factory, **kwargs)
#
# - AES_decrypt(base_cipher_state, in, out, length)
# - AES_encrypt(base_cipher_state, in, out, length)
# - AES_start_operaion(key) --> base_cipher_state
# - AES_stop_operation(base_cipher_state)
# - CBC_decrypt(mode_state, in, out, length)
# - CBC_encrypt(mode_state, in, out, length)
# - CBC_start_operation(base_cipher_state) --> mode_state
# - CBC_stop_operation(mode_state)
# 1. A base cipher (such as AES)
# 2. A mode of operation (such as CBC)
# A block cipher is instantiated as a combination of:
# Both items are implemented as C modules.
# pointers to encrypt/decrypt/stop) followed by cipher-specific data.
# The API of #1 is (replace "AES" with the name of the actual cipher):
# The API of #2 is (replace "CBC" with the name of the actual mode):
# Where base_cipher_state is AES_State, a struct with BlockBase (set of
# where mode_state is a a pointer to base_cipher_state plus mode-specific data.
_extra_modes = {
_modes = {
}
def _create_cipher(factory, key, mode, *args, **kwargs):
from Cryptodome.Cipher._mode_cbc import _create_cbc_cipher
from Cryptodome.Cipher._mode_ccm import _create_ccm_cipher
from Cryptodome.Cipher._mode_cfb import _create_cfb_cipher
from Cryptodome.Cipher._mode_ctr import _create_ctr_cipher
from Cryptodome.Cipher._mode_eax import _create_eax_cipher
from Cryptodome.Cipher._mode_ecb import _create_ecb_cipher
from Cryptodome.Cipher._mode_gcm import _create_gcm_cipher
from Cryptodome.Cipher._mode_ocb import _create_ocb_cipher
from Cryptodome.Cipher._mode_ofb import _create_ofb_cipher
from Cryptodome.Cipher._mode_openpgp import _create_openpgp_cipher
from Cryptodome.Cipher._mode_siv import _create_siv_cipher
