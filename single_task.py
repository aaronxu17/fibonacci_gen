## Choose single task ##
from flask.ext.restful import reqparse, abort, Api, Resource
from index_table import *


class SingleTask(Resource):
    # Error message for no-exist task_id
    def abort_if_task_doesnt_exist(self,task_id):
        if task_id not in INDEX:
            abort(404, message="Task {} does not exist".format(task_id))
    def get(self,task_id):
        self.abort_if_task_doesnt_exist(task_id)
        if task_id=='task1':
            return("Please input a positive integer number with the format:</number>")
        else:
            return INDEX[task_id]