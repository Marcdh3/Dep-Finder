'''
Runs installation tests for depfinder package.
'''

import unittest

from . import test_finder

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromModule(module=test_finder)
    runner = unittest.TextTestRunner()
    runner.run(suite)
