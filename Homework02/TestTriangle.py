# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from triangle_classifier import classify_triangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):
    # define multiple sets of tests as functions with names that begin

    def testRightTriangleA(self): 
        self.assertEqual(classify_triangle(3,4,5),'Right','3,4,5 is a Right triangle')
        
    def testEquilateralTriangles(self): 
        self.assertEqual(classify_triangle(1,1,1),'Equilateral','1,1,1 should be equilateral')

    def testNegativeTriangles(self): 
        self.assertEqual(classify_triangle(-1,1,1),'InvalidInput','-1,1,1 should be InvalidInput')
    
    def testOversizeTriangles(self): 
        self.assertEqual(classify_triangle(300,1,1),'InvalidInput','300,1,1 should be InvalidInput')

    def testStringInputTriangles(self): 
        self.assertEqual(classify_triangle('a',1,1),'InvalidInput','\'a\',1,1 should be InvalidInput')
    
    def testNonTriangles(self): 
        self.assertEqual(classify_triangle(10,1,1),'NotATriangle','10,1,1 should be NotATriangle')
    
    def testIsoTriangles(self): 
        self.assertEqual(classify_triangle(10,10,12),'Isoceles','10,10,12 should be Isoceles')

    def testScaleTriangles(self): 
        self.assertEqual(classify_triangle(2,3,4),'Scalene','2,3,4 should be Scalene')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

