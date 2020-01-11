import unittest

from depfinder import finder as df

class depfinderTest(unittest.TestCase):
    def test_find_deps(self):
        self.assertEqual(df.find_deps('depfinder'), ['coverage'])
