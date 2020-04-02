import unittest
from Question6 import output

class TestOutput(unittest.TestCase):
    def test_output1(self):
        self.assertEqual(output(1, [5, 8, 9, 12]), '12')

    def test_output2(self):
        self.assertEqual(output(3, [12, 54, 3, 4, 6, 7]), '54, 12, 7')

    # This doesn't cover every possible mis-use, but it handles some of the common ones
    def test_exception_for_illegal_args(self):
        self.assertRaises(Exception, output(-1, [12, 54]))
