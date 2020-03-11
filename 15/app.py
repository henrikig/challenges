from flask import Flask, render_template, request
import json


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    todo = None
    if request.method == 'POST':
        todo = request.form.get('todo')
    with open('todo.txt', 'r') as f:
        todos = f.read()
        todos = json.loads(todos) if todos else dict()
    if todo:
        if todo in todos:
            todos[todo] = not todos[todo]
        else:
            todos[todo] = False
        with open('todo.txt', 'w') as f:
            json.dump(todos, f)

    return render_template('todos.html', todos=todos)


@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', name=username.capitalize())



if __name__ == '__main__':
    app.run(debug=True)
