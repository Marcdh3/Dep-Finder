import os
import unittest

import depfinder.finder as finder

class FinderTest(unittest.TestCase):
    def test_find_deps(self):
        deps = finder.find_deps('depfinder')
        ground_truth = ['coverage', 'chardet', 'idna', 'urllib3', 
                          'requests', 'docopt', 'coveralls']
        result = [True for package in ground_truth if package in deps]
        self.assertEqual(sum(result), len(result))
    
    def test_generate_requirements(self):
        deps = ['chardet', 'coverage', 'coveralls', 'depfinder','docopt',
                'idna', 'requests', 'urllib3']
        ground_truth  = ['chardet==', 'coverage==', 'coveralls==', 
                         'depfinder==', 'docopt==', 'idna==', 'requests==',
                         'urllib3==']
        reqs = finder.generate_requirements(deps)
        result = [True for package in ground_truth if ground_truth in reqs]
        self.assertEqual(sum(result), len(result))
