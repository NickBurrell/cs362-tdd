import unittest

from check_pwd import check_pwd

class Main(unittest.TestCase):
        
    def test_nonempty(self):
        self.assertFalse(check_pwd(""))
    
    def test_contains_upper_1(self):
        self.assertTrue(check_pwd("abcdefgHi"))

    def test_contains_upper_2(self):
        self.assertTrue(check_pwd("abcdefghijklMNOP"))

    def test_contains_upper_3(self):
        self.assertFalse(check_pwd("AAAAAAA"))


if __name__ == "__main__":
    unittest.main()
