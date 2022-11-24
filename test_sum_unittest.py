#Jordy Jordan
#The unittest part
import unittest


class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()

#This is the following error when the file is run

#Exception has occurred: SystemExit
#True
#  File "C:\Users\jorda\Documents\ACODE\IvyTechCode\M05 Programming Assignment - Testing\test_sum_unittest.py", line 13, in <module>
#    unittest.main()

#terminal
#Ran 2 tests in 0.003s
#
#FAILED (failures=1)




#The nose part
######pip install nose2######
#Installing collected packages: nose2
#Successfully installed nose2-0.12.0

######python -m nose2######
#PS C:\Users\jorda\Documents\ACODE\IvyTechCode\M05 Programming Assignment - Testing> python -m nose2
#it gave me an error

#..F
#======================================================================
#FAIL: test_sum_tuple (test_sum_unittest.TestSum.test_sum_tuple)       
#----------------------------------------------------------------------
#Traceback (most recent call last):
#  File "C:\Users\jorda\Documents\ACODE\IvyTechCode\M05 Programming Assignment - Testing\test_sum_unittest.py", line 10, in test_sum_tuple
#    self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")
#AssertionError: 5 != 6 : Should be 6

#----------------------------------------------------------------------
#Ran 3 tests in 0.000s

#FAILED (failures=1)



#The pytest part
#nothing appears since everything is successful 
def test_sum():
    assert sum([1, 2, 3]) == 6, "Should be 6"

def test_sum_tuple():
    assert sum((1, 2, 2)) == 6, "Should be 6"