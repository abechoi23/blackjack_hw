from whiteboard import *
# change whiteboard to python file name, you can change * to function name
import unittest

class CalculatorTest(unittest.TestCase):

    def test_sum_unique(self):
        result1 = sum_unique([3, 4, 3, 6])
        self.assertEqual(result1, 10)
        result2 = sum_unique([1,2,3,3,4,4,4])
        self.assertEqual(result2, 3)
        
    def test_no_occurences(self):
        result = sum_unique([1,2,3,4])
        self.assertEqual(result, 10)

unittest.main()