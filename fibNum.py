from itertools import islice

def fib(pre=0, cur=1):
    yield pre
    while True:
        yield cur
        pre, cur = cur, pre + cur

while True:       
	getInput = raw_input("Please input the length of Fibonacci Sequence:")
	if getInput.isdigit():
		num=int(getInput)
		fibonacci_numbers = list(islice(fib(), num))
		print(fibonacci_numbers)
		break
	else:
		print("Please input positive integer number!")




