import unittest

#import coveralls

#coveralls.wear()
class DepTest(unittest.TestCase):
    def test_pass(self):
        self.assertTrue(True)

if __name__ == "__main__":
    unittest.main()
