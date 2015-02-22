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


# Here's the "unit" to test.
def fib(pre=0, cur=1):
    yield pre
    while True:
        yield cur
        pre, cur = cur, pre + cur

TODOS = {
    'todo1': {'task1': 'Generate N Fibonacci Numbers'},
    'todo2': {'task2': 'Hellow World!'},
    'todo3': {'task3': 'Adding more tasks...'},
}

	
		
# Here's the "unit tests".
class FibTestCase(unittest.TestCase):
	# we test five Fibonacci numbers
    def test_five_fibonacci_numbers(self):
	# correct Fibonacci numbers for reference
		fib_correct = [0,1,1,2,3]  
	# generate five Fibonacci numbers from function fib()
		fib_generate = list(islice(fib(), 5))
		self.assertEqual(fib_correct,fib_generate,"Incorrect Fibonacci Numbers Generated!")
    
    # test input a negative number
    def test_input_negative_number(self):
        fib_n = '-5'
        self.assertFalse(fib_n.isdigit())
    
    # test input non-number
    def test_inout_non_number(self):
        fib_n = 'abc'
        self.assertFalse(fib_n.isdigit())
        
    # test input todo_id not exist in to-do list    
    def test_input_wrong_todo_id(self):
        todo_id = 'todo5'
        self.assertNotIn(todo_id, TODOS)

if __name__ == '__main__':
    unittest.main()