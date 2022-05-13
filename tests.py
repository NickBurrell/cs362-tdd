import unittest

from check_pwd import check_pwd

class Main(unittest.TestCase):
        
    def test_nonempty(self):
        self.assertFalse(check_pwd(""))
    
    def test_contains_upper_1(self):
        self.assertTrue(check_pwd("1`abcdefgHi"))

    def test_contains_upper_2(self):
        self.assertTrue(check_pwd("1abcdefg=hijklMNOP"))

    def test_contains_upper_3(self):
        self.assertFalse(check_pwd("AAAAAA+A"))

    def test_contains_lower_1(self):
        self.assertTrue(check_pwd("1abcdefgH_i"))

    def test_contains_lower_2(self):
        self.assertTrue(check_pwd("1a%bcdefgh1ijklMNOP"))

    def test_contains_lower_3(self):
        self.assertFalse(check_pwd("1AAAAAA-A"))

    def test_contains_digit_1(self):
        self.assertTrue(check_pwd("abcdefg@H2"))

    def test_contains_digit_2(self):
        self.assertTrue(check_pwd("abcdefgh&ijklMNOP1"))

    def test_contains_digit_3(self):
        self.assertFalse(check_pwd("AAAAAAA"))

    def test_contains_symbol_1(self):
        self.assertTrue(check_pwd("abcdefg^H2"))

    def test_contains_symbol_2(self):
        self.assertTrue(check_pwd("bghi()jklMNOP1"))

    def test_contains_symbol_3(self):
        self.assertFalse(check_pwd("AAAAAAA-"))

    def test_contains_other(self):
        self.assertFalse(check_pwd("1-aBcDeF,"))




if __name__ == "__main__":
    unittest.main()
