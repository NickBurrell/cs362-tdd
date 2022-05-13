import unittest

from check_pwd import check_pwd

class Main(unittest.TestCase):
        
    def test_nonempty(self):
        self.assertFalse(check_pwd(""))
    
    def test_contains_upper_1(self):
        self.assertTrue(check_pwd("1abcdefgHi"))

    def test_contains_upper_2(self):
        self.assertTrue(check_pwd("1abcdefghijklMNOP"))

    def test_contains_upper_3(self):
        self.assertFalse(check_pwd("AAAAAAA"))

    def test_contains_lower_1(self):
        self.assertTrue(check_pwd("1abcdefgHi"))

    def test_contains_lower_2(self):
        self.assertTrue(check_pwd("1abcdefghijklMNOP"))

    def test_contains_lower_3(self):
        self.assertFalse(check_pwd("1AAAAAAA"))

    def test_contains_digit_1(self):
        self.assertTrue(check_pwd("abcdefgH2"))

    def test_contains_digit_2(self):
        self.assertTrue(check_pwd("abcdefghijklMNOP1"))

    def test_contains_digit_3(self):
        self.assertFalse(check_pwd("AAAAAAA"))



if __name__ == "__main__":
    unittest.main()
