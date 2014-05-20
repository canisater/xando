'''
Created on 19 May 2014

@author: canisater
'''
import unittest
import model

class Test(unittest.TestCase):


    def setUp(self):
        self.m = model()


    def tearDown(self):
        pass


    def testName(self):
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()