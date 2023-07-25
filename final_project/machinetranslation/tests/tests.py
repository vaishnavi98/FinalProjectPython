import unittest
from deep_translator import MyMemoryTranslator
from machinetranslation.translator import english_to_french,french_to_english
class TranslatorTestCase(unittest.TestCase):
    def test_translation(self):
        result = MyMemoryTranslator('en-IN', 'fr-FR').translate(english_to_french('Hello'))
        self.assertEqual(result, 'Bonjour')
        result1 = MyMemoryTranslator('en-IN', 'fr-FR').translate(english_to_french('Madam'))
        self.assertEqual(result1, 'Madame')
    def test_translation1(self):
        result = MyMemoryTranslator('fr-FR','en-IN').translate(french_to_english('Bonjour'))
        self.assertEqual(result, 'Hello')
        result1 = MyMemoryTranslator('fr-FR','en-IN').translate(french_to_english('Madame'))
        self.assertEqual(result1, 'Mrs')
if __name__ == '__main__':
    unittest.main()
