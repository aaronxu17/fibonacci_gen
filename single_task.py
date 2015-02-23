## Choose single task ##

class SingleTask:
    def get(self,task_id):
        abort_if_task_doesnt_exist(task_id)
        if task_id=='task1':
            return("Please input a positive integer number with the format:</number>")
        else:
            return MENU[task_id]