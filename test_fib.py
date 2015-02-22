################# Unit Testing for Fibonacci number generating function #################
#################        Created by Aaron Yiran Xu, Feb. 21, 2015       #################

import unittest
from itertools import islice

# Here's the "unit" to test.
def fib(pre=0, cur=1):
    yield pre
    while True:
        yield cur
        pre, cur = cur, pre + cur

		
def inputNum(Fib_n)
	if Fib_n.isdigit():
		num=int(Fib_n)
		fibonacci_numbers = list(islice(fib(), num))
		return fibonacci_numbers
	else:
		return("Input Error! Please input positive integer number with the format: </number>!")		
		
# Here's the "unit tests".
class FibTestCase(unittest.TestCase):
	# we test five Fibonacci numbers
    def test_five_fibonacci_numbers(self):
	# correct Fibonacci numbers for reference
		fib_correct = [0,1,1,2,3]  
	# generate five Fibonacci numbers from function fib()
		fib_generate = list(islice(fib(), 5))
		self.assertEqual(fib_correct,fib_generate,"Incorrect Fibonacci Numbers Generated!")
	def test_input_negative_number(self):
		fib_n = [-5]
		self.assertTrue()
		

if __name__ == '__main__':
    unittest.main()