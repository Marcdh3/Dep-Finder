import unittest

#import coveralls

#coveralls.wear()
class DepTest(unittest.TestCase):
    def test_pass(self):
        self.assertTrue(True)

    def test_pass(self):
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()
