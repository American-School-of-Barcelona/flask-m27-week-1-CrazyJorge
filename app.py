from flask import Flask, render_template, request, session, redirect, url_for

app = Flask(__name__)
app.secret_key = "super-secret-key"

# TODO: Add your routes below this line

@app.route('/')
def index():
    return render_template("index.html",)

@app.route('/greet')
def greet():
    if "name" in request.args:
        session["name"] = request.args.get("name")

    name = session.get("name")

    if not name:
        return redirect(url_for("index"))
    
    return render_template("greet.html", name=name)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/tasks')
def tasks():
    return render_template("tasks.html")

if __name__ == "__main__":
    app.run(debug=True)
