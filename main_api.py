## Web Service ##

from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
import single_task

app = Flask(__name__)
api = Api(app)

# menu
INDEX = {
    'task1': {'#1': 'Generate N Fibonacci Numbers'},
    'task2': {'#2': 'Hello World!'},
    'task3': {'#3': 'Adding more tasks...'},
}

# Error message for no-exist task_id
def abort_if_task_doesnt_exist(task_id):
    if task_id not in INDEX:
        abort(404, message="Task {} does not exist".format(task_id))
        
parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


class Index(Resource):
    def get(self):
        return INDEX

api.add_resource(Index,'/')
api.add_resource(single_task.SingleTask, '/<string:task_id>')
# api.add_resource(fibo_gen.FiboGen,'/index/task1/<string:Fib_n>')

if __name__=='__main__':
    app.run()