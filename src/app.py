from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/todos', methods=['GET', 'POST'])
def handle_todos():
    if request.method == 'GET':
        response_body = todos
        return response_body
    if request.method == 'POST':
        request_body = request.json
        print("Incoming request with the following body", request_body)
        todos.append(request_body)
        response_body = todos
        return response_body


@app.route('/todos/<int:position>', methods=['GET','DELETE'])
def handle_todos_position(position):
    if request.method == 'GET':
        response_body = todos[position]
        # response_body = todos -> al ser list/dict lo interpreta como json directamente
        return response_body
    if request.method == 'DELETE':
        print("This is the position to delete: ",position)
        del todos[position]
        response_body = todos
        return response_body

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)