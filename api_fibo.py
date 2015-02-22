#################  Fibonacci number generating based on Flask rest framework #################
#################        Created by Aaron Yiran Xu, Feb. 21, 2015       #################

from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
from itertools import islice

app = Flask(__name__)
api = Api(app)

# To-do-list, each corresponds to one task.
TODOS = {
    'todo1': {'task1': 'Generate N Fibonacci Numbers'},
    'todo2': {'task2': 'Hellow World!'},
    'todo3': {'task3': 'Adding more tasks...'},
}

# Error message if to-do-id is not in to-do-list
def abort_if_todo_doesnt_exist(todo_id):
    if todo_id not in TODOS:
        abort(404, message="Todo {} doesn't exist".format(todo_id))

parser = reqparse.RequestParser()
parser.add_argument('task', type=str)

# Fibonacci number generating function
def fib(pre=0, cur=1):
    yield pre
    while True:
        yield cur
        pre, cur = cur, pre + cur

# TodoList
#   shows a list of all todos
class TodoList(Resource):
    def get(self):
        return TODOS

# Todo
#   show a single todo item 
class Todo(Resource):
    def get(self, todo_id):
        abort_if_todo_doesnt_exist(todo_id)
	if todo_id=='todo1':
		return ("Please input positive integer number with the format: </number>!")
	else:
		return TODOS[todo_id]


# Generate N Fibonacci Numbers, start from 0
# return the Fibonacci sequence
class FibGen(Resource):
	def get(self, Fib_n):
		if Fib_n.isdigit():
			num=int(Fib_n)
			fibonacci_numbers = list(islice(fib(), num))
			return fibonacci_numbers
		else:
			return("Input Error! Please input positive integer number with the format: </number>!")
		


##
## Actually setup the Api resource routing here
api.add_resource(TodoList, '/todos')
api.add_resource(Todo, '/todos/<string:todo_id>')
api.add_resource(FibGen, '/todos/todo1/<string:Fib_n>')


if __name__ == '__main__':
    app.run()