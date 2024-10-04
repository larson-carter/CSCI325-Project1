from unittest import TestCase
from CarterProject1 import (keyword, columnar, vigenere, keywordDecrypt, columnarDecrypt, vigenereDecrypt)


class TestCiphers(TestCase):
    def test_keyword(self):
        self.assertEqual(
            keyword("Whale", "Hello! I am testing this program."),
            "Dejjn! F wk sersfmc sdfr oqncqwk.",
            "Keyword cipher encryption failed"
        )

    def test_columnar(self):
        self.assertEqual(
            columnar("Whale", "Hello! I am testing this program."),
            "lItnio.oas re ihrml egsgH!mttpa",
            "Columnar cipher encryption failed"
        )

    def test_vigenere(self):
        self.assertEqual(
            vigenere("Whale", "Hello! I am testing this program."),
            "Dllws! E hm eioaiyk poid tnvgcei.",
            "Vigenere cipher encryption failed"
        )

    def test_keyword_decrypt(self):
        self.assertEqual(
            keywordDecrypt("Whale", "Dejjn! F wk sersfmc sdfr oqncqwk."),
            "Hello! I am testing this program.",
            "Keyword cipher decryption failed"
        )

    def test_columnar_decrypt(self):
        self.assertEqual(
            columnarDecrypt("Whale", "lItnio.oas re ihrml egsgH!mttpa"),
            "Hello! I am testing this program.",
            "Columnar cipher decryption failed"
        )

    def test_vigenere_decrypt(self):
        self.assertEqual(
            vigenereDecrypt("Whale", "Dllws! E hm eioaiyk poid tnvgcei."),
            "Hello! I am testing this program.",
            "Vigenere cipher decryption failed"
        )

    def test_keyword_all(self):
        encryptedText = keyword("Whale", "Hello! I am testing this program.")
        decryptedText = keywordDecrypt("Whale", encryptedText)

        self.assertEqual(encryptedText, "Dejjn! F wk sersfmc sdfr oqncqwk.", "Keyword cipher encryption failed")
        self.assertEqual(decryptedText, "Hello! I am testing this program.", "Keyword cipher decryption failed")
