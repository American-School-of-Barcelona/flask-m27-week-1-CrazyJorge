from flask import Flask, render_template, request

app = Flask(__name__)

# TODO: Add your routes below this line

@app.route('/greet/<name>')
def greet():
    name = request.args.get("name")
    return render_template("greet.html", name=name)

@app.route('/')
def index():
    name = request.args.get("name")
    return render_template("index.html", name=name)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/tasks')
def tasks():
    return render_template("tasks.html")

if __name__ == "__main__":
    app.run(debug=True)
