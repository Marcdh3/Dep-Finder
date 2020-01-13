'''
Runs installation tests for depfinder package.
'''

import unittest

import test_finder
import test_main

if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests([
        loader.loadTestsFromModule(module=test_finder),
        loader.loadTestsFromModule(module=test_main)
    ])
    runner = unittest.TextTestRunner()
    runner.run(suite)
