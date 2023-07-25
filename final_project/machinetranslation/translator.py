"""This file is to translate"""
from deep_translator import MyMemoryTranslator
def english_to_french(english_text):
    """ translate french to english"""
    french_text = MyMemoryTranslator(source='en-IN',target='fr-FR').translate(english_text)
    return french_text
def french_to_english(french_text):
    """ translate french to english"""
    english_text = MyMemoryTranslator(source='fr-FR',target='en-IN').translate(french_text)
    return english_text
	