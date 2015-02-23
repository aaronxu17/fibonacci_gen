################# Unit Testing for Fibonacci number generating function #################
#################        Created by Aaron Yiran Xu, Feb. 21, 2015       #################
## This unit tests the input number n and input todo_id
## test 1: input n = 5, return right Fibonacci numbers
## test 2: input n = -5
## test 3: input n = abc
## test 4: input todo_id = todo5
#########################################################################################

import unittest
from itertools import islice
import fibo_func
import os,sys

INDEX = {
    'task1': {'#1': 'Generate N Fibonacci Numbers'},
    'task2': {'#2': 'Hellow World!'},
    'task3': {'#3': 'Adding more tasks...'},
}
	
		
# Here's the "unit tests".
class TestCase(unittest.TestCase):
	# we test five Fibonacci numbers
    def test_five_fibonacci_numbers(self):
	# correct Fibonacci numbers for reference
		fib_correct = [0,1,1,2,3]  
	# generate five Fibonacci numbers from function fib()
		fib_generate = list(islice(fibo_func.fib(), 5))
		self.assertEqual(fib_correct,fib_generate,"Incorrect Fibonacci Numbers Generated!")
    
    # test input a negative number
    def test_input_negative_number(self):
        fib_n = '-5'
        self.assertFalse(fib_n.isdigit())
    
    # test input non-number
    def test_inout_non_number(self):
        fib_n = 'abc'
        self.assertFalse(fib_n.isdigit())
        
    # test input float number
    def test_input_float_number(self):
        fib_n = '12.0'
        self.assertFalse(fib_n.isdigit())
        
    # test input very large number
    def test_input_large_number(self):
        fib_n = 1000000000000000000000
        self.assertGreaterEqual(fib_n,sys.maxint)
        
    # test input todo_id not exist in to-do list    
    def test_input_wrong_todo_id(self):
        todo_id = 'task5'
        self.assertNotIn(todo_id, INDEX)

if __name__ == '__main__':
    unittest.main()