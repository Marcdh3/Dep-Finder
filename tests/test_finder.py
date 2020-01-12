import unittest

from depfinder import finder as df

class FinderTest(unittest.TestCase):
    def test_find_deps(self):
        finder = df.find_deps('depfinder')
        ground_truth = ['coverage', 'chardet', 'idna', 'urllib3', 
                          'requests', 'docopt', 'coveralls']
        finder.sort()
        ground_truth.sort()
        self.assertEqual(finder, ground_truth)
