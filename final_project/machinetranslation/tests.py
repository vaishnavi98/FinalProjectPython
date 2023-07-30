import unittest

from translator import english_to_french, french_to_english
class TranslatorTestCase(unittest.TestCase):
    def test_translation(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")
        self.assertNotEqual(english_to_french("Thank you"), "Merci")
    def test_translation1(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertNotEqual(french_to_english("Merci"), "Thanks")
if __name__ == '__main__':
    unittest.main()
