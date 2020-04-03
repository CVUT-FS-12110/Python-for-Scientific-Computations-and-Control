from flask import Flask, render_template

app = Flask(__name__) # create our application named __name__ ("helloworld")

@app.route("/home") # home route
def home():
    # flasks default folder for templates is called "/templates"
    return render_template("home.html") # render template from /templates/home.html


app.run(debug=True) # run server, debug is set to True