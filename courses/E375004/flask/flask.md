# Server applications 

## flask, jinja (+ SQLAlchemy and WTForms)

## Before we start
Before we start I recommend you to create new empty virtual enviroment (I usually name it ".venv")

```
python -m venv .venv
```

Activate it:

```
/.venv/Scripts/activate
```

Install flask:

```
pip install flask
```

This usualy works for windows users. If you are using Ubuntu (or any other Linx distribution) or Mac, find how to create and activate virtual enviroment on those platforms.

## Introduction

### What is flask?
On the internet, you can find something as *"Flask is microweb framework for building websites in python"*. We can think of a flask as ready-to-go python library for simple web application development.

### Why flask and not Django?
Django is perfect framwork. For ours purposes is flask better. Flask is easier to start with and much more lightweight. If you are serius in web application development, you should new Django as well though.

### Please pay attention to the official websites (mainly documentation)

- [Flask](https://flask.palletsprojects.com/)
- [Jinja](https://jinja.palletsprojects.com/)

### Tutorials
There are many tutorials out there, search for them and use them as a study material. In my opinion they are good enough. I recommend for example this one (to start with):
  - [Flask Tutorial #1](https://www.youtube.com/watch?v=mqhxxeeTbu0) - we will start with similar project
Don't be scared to pick any other that will suit you more.

## Hello world!
Our first application will consist from only one .py script:
    - [flask Hello World!](helloworld/helloworld.py)

Try to run it and pay attention to code, study all function you don't understand:

```
python helloworld.py
```

In command line you should see something like:

```
 * Serving Flask app "helloworld" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 231-816-225
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Our application will run on local host.

Open your web browser and try to type:
- http://127.0.0.1:5000/home
- http://127.0.0.1:5000/greetings/adam
- http://127.0.0.1:5000/greetings/eva

How is server reacting and why?

## HTML and Jinja
At this point, you hopefully read something about flask and you know, that flask is usually used for backend of our server application. That means, that flask manages all those things on the server side. In our case, flask basically does everything. What happens with request?

1. We generate *request*:
    For example http://127.0.0.1:5000/home
2. Flask knows that if it gets this request, it should run function called *home* (it's written in the code)
3. Function *home* returns string "Hello world!"
4. Our browser represents somehow the response (in this case simple string)

Perfect, now when we use same logic, we can return whole HTML page (same as string), right? For those purposes is really important function [render_template](https://flask.palletsprojects.com/en/1.1.x/api/#flask.render_template) (read the docs).

### Second application - simpleapp
Our second application will be whole folder:
- [link to folder](simpleapp/)
Now it is really important to copy whole content of that folder.

We will run our application called "simpleapp":

```
python simpleapp.py
```

Again, we should see something like:
```
 * Serving Flask app "simpleapp" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 231-816-225
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Open browser and type:
- http://127.0.0.1:5000/home

Now try to open file "templates/home.html" from this folder manualy. Are there any differences?

Now try to type:
- http://127.0.0.1:5000/jinja/adam
- http://127.0.0.1:5000/jinja/jan

Compare to static file "templates/jinja.html". Are there any differences?

In the second case, we can see what *Jinja* is for. It can take something  (in our case simple string *response*) and put it to html to the place where *{{ response }}* is.

Jinja is capable of much more of course. Read the official documentation.

## Homework - Task flask

The following task is (because of lack of in-person lectures) harder, but I created the task in such a shape, that you can find very similar projects on the internet solved. Please, try to do some home study and solve it by yourself. If it will be too hard, you can google it and recycle some solution out there.

Study at home:
  - [SQLAlchemy](https://www.sqlalchemy.org/) and **ORM**, we won't need classical SQL syntax, but you can read about SQL databases as well
  - [WTForms](https://wtforms.readthedocs.io/en/stable/) (forms and how they work)
  - [Bootstrap](https://getbootstrap.com/) (optional, only for the people interested in better design)

Create a web application called **warehouse** with flask, SQLAlchemy and WTForms (eventually others):
  - This application will have form with submit button.
  - Using this form, users will be able to add item to the warehouse (SQL database). Every item will be represented by (at least) **name** and **quantity** (you can add more, for example material, date, ...)
  - After user adds item to the warehouse, page will refresh and HTML table of all items will be updated (it is homework, lets assume we will have only few items in the warehouse)
  - (optional) add **DELETE** button to every item in HTML table.

Even if it is unconventional, please, program the whole app as **one-script** for reading and checking purposes.
