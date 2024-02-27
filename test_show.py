import unittest
import show

class ShowTest(unittest.TestCase):
    def test_empty_string():
        self.assertEqual(show.name(" "), " ")