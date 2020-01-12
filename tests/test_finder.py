import unittest

import depfinder.finder as df

class FinderTest(unittest.TestCase):
    def test_find_deps(self):
        deps = df.find_deps('depfinder')
        ground_truth = ['coverage', 'chardet', 'idna', 'urllib3', 
                          'requests', 'docopt', 'coveralls']
        deps.sort()
        ground_truth.sort()
        self.assertEqual(deps, ground_truth)
