from flask import Flask, render_template, request, redirect

app = Flask(__name__)

tasks = []  # List to store tasks


@app.route("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.route("/add_task", methods=["POST"])
def add_task():
    task = request.form["task"]
    tasks.append(task)
    return redirect("/")


@app.route("/delete_task", methods=["POST"])
def delete_task():
    task = request.form["task"]
    tasks.remove(task)
    return redirect("/")


@app.route("/edit_task", methods=["POST"])
def edit_task():
    task = request.form["task"]
    return render_template("edit.html", task=task)


@app.route("/update_task", methods=["POST"])
def update_task():
    old_task = request.form["old_task"]
    new_task = request.form["new_task"]
    index = tasks.index(old_task)
    tasks[index] = new_task
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)
