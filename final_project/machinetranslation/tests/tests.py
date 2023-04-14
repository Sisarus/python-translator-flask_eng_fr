import unittest
import sys

sys.path.append('../')

from translator import french_to_english, english_to_french

class TestEnglishToFrench(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(english_to_french("Cat"), "Hello")
        self.assertEqual(english_to_french('Hello'), 'Bonjour')

class TestFrenchToEnglish(unittest.TestCase): 
    def test1(self): 
        self.assertNotEqual(french_to_english("Cato"), "Bonjour")
        self.assertEqual(french_to_english('Bonjour'), 'Hello')

unittest.main()
