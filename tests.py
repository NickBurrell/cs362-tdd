import unittest

from check_pwd import check_pwd

class Main(unittest.TestCase):
    def test_nonempty(self):
        self.assertFalse(check_pwd(""))

if __name__ == "__main__":
    unittest.main()
