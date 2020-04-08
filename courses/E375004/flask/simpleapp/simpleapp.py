from flask import Flask, render_template

app = Flask(__name__) # create our application named __name__ ("helloworld")

@app.route("/home") # home route
def home():
    # flasks default folder for templates is called "/templates"
    return render_template("home.html") # render template from /templates/home.html


@app.route("/jinja/<name>")
def jinja(name):
    if name == "adam":
        response = f"Hello {name}"
    else:
        response = f"I am sorry, I dont know you {name}"
    return render_template("jinja.html", response=response)
    
app.run(debug=True) # run server, debug is set to True