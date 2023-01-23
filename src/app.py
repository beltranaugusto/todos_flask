from flask import Flask, request, jsonify

app = Flask(__name__)

todos = [
    {
        "done": True,
        "label": "Sample Todo 1"
    },
    {
        "done": True,
        "label": "Sample Todo 2"
    }
]

@app.route('/todos', methods=['GET'])
def get_todos():
    resp = jsonify(todos)
    return resp

@app.route('/add_todo', methods=['POST'])
def add_todo():
    body = request.get_json()
    if 'done' and 'label' in body:
        todos.append(body)
        resp = jsonify(todos)
        return resp, 200
    else:
        return 'Json content not accepted, done or label missing.', 400

@app.route('/delete_todo/<int:position>', methods=['POST'])
def delete_todo(position=None):
    todos.pop(position)
    resp = jsonify(todos)
    return resp, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="3001", debug=True)