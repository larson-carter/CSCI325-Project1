from unittest import TestCase
from CarterProject1 import (keyword, columnar, vigenere, keywordDecrypt, columnarDecrypt, vigenereDecrypt)

class Test(TestCase):
    def test_keyword(self):
        key = "Whale"
        plaintext = "Hello! I am testing this program."
        expectedOutput = "Dejjn! F wk sersfmc sdfr oqncqwk."
        result = keyword(key, plaintext)
        self.assertEqual(result, expectedOutput, "Keyword cipher encryption failed")

    def test_columnar(self):
        key = "Whale"
        plaintext = "Hello! I am testing this program."
        expectedOutput = "lItnio.oas re ihrml egsgH!mttpa"
        result = columnar(key, plaintext)
        self.assertEqual(result, expectedOutput, "Columnar cipher encryption failed")

    def test_vigenere(self):
        key = "Whale"
        plaintext = "Hello! I am testing this program."
        expectedOutput = "Dllws! E hm eioaiyk poid tnvgcei."
        result = vigenere(key, plaintext)
        self.assertEqual(result, expectedOutput, "Vigenere cipher encryption failed")

    def test_keyword_decrypt(self):
        self.fail()

    def test_columnar_decrypt(self):
        self.fail()

    def test_vigenere_decrypt(self):
        self.fail()
