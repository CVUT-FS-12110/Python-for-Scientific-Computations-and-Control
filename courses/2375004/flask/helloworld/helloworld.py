from flask import Flask

app = Flask(__name__) # create our application named __name__ ("helloworld")

@app.route("/home") # home route
def home():
    return "Hello World!"

@app.route("/greetings/<name>") # greetings route with route to any name
def greetings(name):
    return f"Hello {name}!"

app.run(debug=True) # run server, debug is set to True