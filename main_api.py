## Web Service ##

from flask import Flask
from flask.ext.restful import reqparse, abort, Api, Resource
import fibo_gen, single_task

app = Flask(__name__)
api = Api(app)

# menu
MENU = {
    'task1': {'Generate N Fibonacci Numbers'},
    'task2': {'Hello World!'},
    'taks3': {'Adding more tasks...'},
}

# Error message for no-exist task_id
def abort_if_task_doesnt_exist(task_id):
    if task_id not in MENU:
        abort(404, message="Task {} does not exist".format(task_id))
        
parser = reqparse.RequestParser()
parser.add_argument('task', type=str)


class Menu(Resource):
    def get(self):
        return MENU

api.add_resource(Menu,'/')
# api.add_resource(single_task.SingleTask, '/<string:task_id>')
# api.add_resource(fibo_gen.FiboGen,'/task1/<string:Fib_n>')

if __name__=='__main__':
    app.run()