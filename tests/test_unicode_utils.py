import unittest
from modules.common.unicode_utils import decompose, filesys_decode, try_encode

class TestUnicodeUtils(unittest.TestCase):

    def test_decompose_str_input(self):
        self.assertEqual(
            decompose("테스트"),
            "테스트"  # NFD (분해형)
        )

    def test_decompose_bytes_input(self):
        input_bytes = "테스트".encode("utf-8")
        output = decompose(input_bytes)
        self.assertTrue(isinstance(output, str))

    def test_filesys_decode_str(self):
        self.assertEqual(filesys_decode("한글"), "한글")

    def test_filesys_decode_bytes_utf8(self):
        byte_path = "시험".encode("utf-8")
        self.assertEqual(filesys_decode(byte_path), "시험")

    def test_filesys_decode_invalid_bytes(self):
        byte_path = b'\xff\xfe\x00\x00'
        self.assertTrue(isinstance(filesys_decode(byte_path), bytes))

    def test_try_encode_success(self):
        encoded = try_encode("테스트", "utf-8")
        self.assertEqual(encoded, b'\xed\x85\x8c\xec\x8a\xa4\xed\x8a\xb8')

    def test_try_encode_fail(self):
        result = try_encode("🔥", "ascii")
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
