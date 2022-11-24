#Jordy Jordan
#test.py
#Executing Your First Test

import unittest
from my_sum import sum

#Understanding Test Output Part
from fractions import Fraction

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]
        result = sum(data)
        self.assertEqual(result, 6)

#New def with Understanding Test Outputs
    def test_list_fraction(self):
        """
        Test that it can sum a list of fractions
        """
        data = [Fraction(1, 4), Fraction(1, 4), Fraction(2, 5)]
        result = sum(data)
        self.assertEqual(result, 1)

if __name__ == '__main__':
    unittest.main()

#I get this error-------->
#Traceback (most recent call last):
#  File "c:\Users\jorda\Documents\ACODE\IvyTechCode\M05 Programming Assignment - Testing\test.py", line 27, in test_list_fraction
#    self.assertEqual(result, 1)
#AssertionError: Fraction(9, 10) != 1

#To me this error basically means that the sum of the fractions on test_list_fraction
#more specifically on result, is not equals to 1 on self.assertEqual(result, 1)
#for example when I run TestSum alone I do not get any erros, instead I get an OK message!
