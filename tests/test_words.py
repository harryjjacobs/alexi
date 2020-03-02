import unittest
from alexi.words import get_random_word, get_rhyming_word

class TestWords(unittest.TestCase):
    def test_random_word_fetch(self):
        self.assertIsNotNone(get_random_word(), "No word fetched")
        self.assertIsNot(get_random_word(), "", "Empty word fetched")

    def test_rhyming_word_fetch(self):
        self.assertIsNotNone(get_rhyming_word("cheese"), "No word fetched")
        self.assertIsNot(get_rhyming_word("cheese"), "", "Empty word fetched")

if __name__ == '__main__':
    unittest.main()