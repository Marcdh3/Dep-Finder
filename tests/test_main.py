import unittest

from depfinder.__main__ import parse

class MainTest(unittest.TestCase):
    def test_parse(self):
        ground_truth = ['-i', 'depfinder']
        args = parse(ground_truth)   
        self.assertEqual(args['input'], 'depfinder')
