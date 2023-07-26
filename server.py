from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

todos = []


@app.route("/")
def home():
    return render_template("index.html", todos=todos)


@app.route("/add", methods=["POST"])
def add():
    todo = request.form['description']
    due_date = request.form['due_date']
    category = request.form['category']
    priority = request.form['priority']
    todos.append({"task": todo, "done": False, "due_date": due_date, "category": category, "priority": priority})
    return redirect(url_for("home"))


@app.route("/edit/<int:index>", methods=["GET", "POST"])
def edit(index):
    todo = todos[index]
    if request.method == "POST":
        todo['task'] = request.form['description']
        todo['due_date'] = request.form['due_date']
        todo['category'] = request.form['category']
        todo['priority'] = request.form['priority']
        return redirect(url_for("home"))
    else:
        return render_template('edit.html', todo=todo, index=index)


@app.route("/check/<int:index>")
def check(index):
    todos[index]['done'] = not todos[index]['done']
    return redirect(url_for('home'))


@app.route("/delete/<int:index>")
def delete(index):
    del todos[index]
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)
