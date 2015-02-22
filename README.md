Web Service
===========

Version 1.0 - Sat 22 Feb 2015

by Aaron Yiran Xu
for EMC technical interview project

Introduction 
------------

This web service is based on Flask rest framework and supports a REST GET call.
There exists multiple tasks, which are listed as to-do list. The task 1 implements 
the Fibonacci sequence generation, where it accepts a input number n and return the 
first n Fibonacci numbers. The task 2 displays "Hello World!" greeting. The task 3 
shows that "more tasks" can be added in the future to extend to a more complex system. 

Requirements
------------
1. Python 2.7 or higher version
2. Flask version 0.8 or greater for Flask-RESTful installation 

Instruction 
-----------
To build the web service, the user should have Python 2.7 or greater version installed 
and install Flask-RESTful framework. This web service can implement the following functions:

1. Get to-do list
-----------------
Put the *.py file into a directory, and launch your Command Prompt to this directory. Then the following command is for you:

$ python api_fibo.py
* Running on http://127.0.0.1:5000/

Now you can test out the APT using curl
$ curl http://localhost:5000/todos

For Windows user, you can open an explorer and input the same url

You can get the to-do list shown as:
{"todo1": {"task1": "Generate N Fibonacci Numbers"}, "todo3": {"task3": "Adding more tasks..."}, "todo2": {"task2": "Hello World!"}}



2. Generate n Fibonacci numbers
-------------------------------
In order to generate Fibonacci numbers, we need to go to task 1:
$ curl http://localhost:5000/todos/todo1

For Windows user, you can open an explorer and input the following url: 
http://localhost:5000/todos/todo1

Then we can get the following message:
"Please input positive integer number with the format: </number>!"

Then, the user can input a non-negative integer number, n(e.g., n=5)
$ curl http://localhost:5000/todos/todo1/5

For Windows user, you can open an explorer and input the same url

Then the web service will return the n Fibonacci numbers:
 [0, 1, 1, 2, 3]

-----------------------------------------------------------------------

Given a negative number or other illegal input, it will respond with an 
appropriate error.

e.g., input -5, abc, 12.4, @1
$ curl http://localhost:5000/todos/todo1/-5

For Windows user, you can open an explorer and input the same url

There will be an input error warning message:
"Input Error! Please input positive integer number with the format: </number>!"

===============================================================================


Unit Testing:
=============
I mainly test the input format for Fibonacci number generator. 
I check the input by calling str.isdigit() method, if it returns False, my code 
will return an error message

Also, if the user input a wrong todo_id, the code will also report an error message 

Future unit-testing is needed if the input is a very huge number, this should be also
considered. 

Another unit test I can think of is test a float number which is n=5.0, this should also
return a n Fibonacci number, but I did not implement in my code.


Maintainability and Expandability:
==================================
The user can add more tasks to current project to implement more functions, and I already
listed taks2, and task3 for reference. 

