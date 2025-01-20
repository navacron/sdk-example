from flask import Flask, jsonify, request
from dataclasses import dataclass
from typing import List, Optional

app = Flask(__name__)

@dataclass
class Todo:
    id: int
    title: str
    completed: bool

todos: List[Todo] = [
    Todo(id=1, title="Learn Flask", completed=False),
    Todo(id=2, title="Build API", completed=False)
]

@app.route('/todos', methods=['GET'])
def get_todos():
    return jsonify([vars(todo) for todo in todos])

@app.route('/todos/<int:todo_id>', methods=['GET'])
def get_todo(todo_id):
    todo = next((todo for todo in todos if todo.id == todo_id), None)
    if todo is None:
        return jsonify({"error": "Todo not found"}), 404
    return jsonify(vars(todo))

@app.route('/todos', methods=['POST'])
def create_todo():
    data = request.get_json()
    new_todo = Todo(
        id=len(todos) + 1,
        title=data['title'],
        completed=False
    )
    todos.append(new_todo)
    return jsonify(vars(new_todo)), 201

if __name__ == '__main__':
    app.run(debug=True, port=5001) 