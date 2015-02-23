## Task 1: Fibonacci Number Class ##
from flask.ext.restful import reqparse, abort, Api, Resource
from itertools import islice
import fibo_func
import os,sys


class FiboGen(Resource):
    def get(self,Fib_n):
        if Fib_n.isdigit():
            num=int(Fib_n)
            if num > sys.maxint:
                return("Please input a smaller number")
            else:
                fibonacci_numbers = list(islice(fibo_func.fib(),num))
                return fibonacci_numbers
        else:
            return("Input Error! Please input a positive integer number")        