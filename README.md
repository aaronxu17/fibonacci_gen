Web Service
===========

Version 1.0 - Sat 22 Feb 2015

by Aaron Yiran Xu
for EMC technical interview project

Introduction 
------------

This web service is based on Flask rest framework and supports a REST GET call.
There exists multiple tasks, which are listed as task list. The task 1 implements 
the Fibonacci sequence generation, where it accepts a input number n and return the 
first n Fibonacci numbers. The task 2 displays "Hello World!" greeting. The task 3 
shows that "more tasks" can be added in the future to extend to a more complex system. 

Requirements
------------
1. Python 2.7 or higher version
2. Flask version 0.8 or greater for Flask-RESTful installation 

Instruction 
-----------
This project includes the following files:
> main_api.py
Web Service API

> single_task.py
Single task introduction
 
> fibo_gen.py
Generate N Fibonacci Numbers, N is a positive integer

> fibo_func.py
Fibonacci Number Generator

> unit_test.py
Unite testing case 

> index_table
Task list


To build the web service, the user should have Python 2.7 or greater version installed 
and install Flask-RESTful framework. This web service can implement the following functions:

1. Get task list
-----------------
Put all *.py files into a directory, and launch your Command Prompt to this directory. Then the following command is for you:

$ python main_api.py
* Running on http://127.0.0.1:5000/

Now you can test out the APT using curl
$ curl http://localhost:5000/

For Windows user, you can open a browser and input the same url

You can get the to-do list shown as:
{
    "task1": {
        "#1": "Generate N Fibonacci Numbers"
    }, 
    "task2": {
        "#2": "Hello World!"
    }, 
    "task3": {
        "#3": "Adding more tasks..."
    }
}


2. Generate n Fibonacci numbers
-------------------------------
In order to generate Fibonacci numbers, we need to go to task 1:
$ curl http://localhost:5000/task1

For Windows user, you can open a browser and input the following url: 
http://localhost:5000/task1

Then we can get the following message:
"Please input a positive integer number with the format:</number>"

Then, the user can input a non-negative integer number, n(e.g., n=5)
$ curl http://localhost:5000/task1/5

For Windows user, you can open a browser and input the same url

Then the web service will return the n Fibonacci numbers:
 [0, 1, 1, 2, 3]

-----------------------------------------------------------------------

Given a negative number or other illegal input, it will respond with an 
appropriate error.

e.g., input -5, abc, 12.0, @1
$ curl http://localhost:5000/task1/-5

For Windows user, you can open a browser and input the same url

There will be an input error warning message:
"Input Error! Please input positive integer number with the format: </number>!"

===============================================================================


Unit Testing:
=============

The following cases are tested in unit_test.py
1. Test whether the fibo_func() generate correct Fibonacci numbers 
2. Test negative number
3. Test non-number input
4. Test float number
5. Test a very large number
6. Test wrong test id


Maintainability and Expandability:
==================================
The user can add more tasks to current project to implement more functions, and I already
listed taks2, and task3 for reference. 

