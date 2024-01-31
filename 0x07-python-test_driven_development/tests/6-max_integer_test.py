#!/usr/bin/python3
"""unittest for the max_integer module"""


import unittest
max_integer = __import__("6-max_integer").max_integer


"""TestMaxInteger
A unit test for testing max_integer function
"""
class TestMaxInteger(unittest.TestCase):

    def test_max(self):
        self.assertEqual(max_integer([5,4,3,2,1]), 5)
        self.assertEqual(max_integer([5,4,3,2,7]), 7)
        self.assertEqual(max_integer([5,4,100,2,1]), 100)

if __name__ == "__main__":
    unittest.main()
