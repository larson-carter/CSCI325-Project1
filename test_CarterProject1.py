from unittest import TestCase
from CarterProject1 import (keyword, columnar, vigenere, keywordDecrypt, columnarDecrypt, vigenereDecrypt)

class Test(TestCase):
    def test_keyword(self):
        self.assertEqual(keyword("Whale", "Hello! I am testing this program."), "Dejjn! F wk sersfmc sdfr oqncqwk.", "Keyword cipher encryption failed")

    def test_columnar(self):
        self.assertEqual(columnar("Whale", "Hello! I am testing this program."), "lItnio.oas re ihrml egsgH!mttpa", "Columnar cipher encryption failed")

    def test_vigenere(self):
        self.assertEqual(vigenere("Whale", "Hello! I am testing this program."), "Dllws! E hm eioaiyk poid tnvgcei.", "Vigenere cipher encryption failed")

    def test_keyword_decrypt(self):
        self.fail()

    def test_columnar_decrypt(self):
        self.fail()

    def test_vigenere_decrypt(self):
        self.fail()
