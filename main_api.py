## Web Service ##

from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
from single_task import *
from fibo_gen import *
from index_table import *

app = Flask(__name__)
api = Api(app)

# menu
# INDEX = {
    # 'task1': {'#1': 'Generate N Fibonacci Numbers'},
    # 'task2': {'#2': 'Hello World!'},
    # 'task3': {'#3': 'Adding more tasks...'},
# }

    
parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


class Index(Resource):
    def get(self):
        return INDEX

api.add_resource(Index,'/')
api.add_resource(SingleTask, '/<string:task_id>')
api.add_resource(FiboGen,'/task1/<string:Fib_n>')

if __name__=='__main__':
    app.run(debug=True)