from flask import Flask, jsonify
from flask import Flask
app = Flask(__name__)
from flask import request

#@app.route('/todos', methods=['GET'])
#def hello_world():
#    return '<h1>Hello!</h1>'

#some_data = { "name": "Bobby", "lastname": "Rixer" }

#@app.route('/myroute', methods=['GET'])
#def hello_world(): 
#  json_text = jsonify(some_data)
#  return json_text

todos = [
    { "label": "My first task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world(): 
  json_text = jsonify(todos)
  return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json
    print("Incoming request with the following body", request_body)
    todos.append(request_body)
    return jsonify(todos)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    print("This is the position to delete:", position)
    todos.pop(position)
    return jsonify(todos)


#como agragar un elemento a una lista en phyton
#como agragar un elemento de tipo diccionario (objeto) a una lista en phyton
#como agragar un ToDo A mi lista todos
#como leer un ToDo en el cuerpo de la solicitud











if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)