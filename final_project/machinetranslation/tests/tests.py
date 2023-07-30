import unittest

from translator import english_to_french, french_to_english
class TranslatorTestCase(unittest.TestCase):
    def test_translation(self):
        self.assertEquals(english_to_french("Hello", "Bonjour"))
        self.assertNotEquals(english_to_french("Madam", "Madame"))
    def test_translation1(self):
        self.assertEquals(french_to_english("Bonjour","Hello"))
        self.assertNotEquals(french_to_english("Madame", "Mrs"))
if __name__ == '__main__':
    unittest.main()
