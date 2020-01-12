import unittest

import depfinder.finder as df

class FinderTest(unittest.TestCase):
    def test_find_deps(self):
        deps = df.find_deps('depfinder')
        ground_truth = ['coverage', 'chardet', 'idna', 'urllib3', 
                          'requests', 'docopt', 'coveralls']
        result = [True for package in ground_truth if package in deps]
        self.assertEqual(sum(result), len(result))
