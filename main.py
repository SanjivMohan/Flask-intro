from flask import Flask, request, jsonify
import json

app = Flask(__name__)

global data

# read data from file and store in global variable data
with open('data.json') as f:
    data = json.load(f)


@app.route('/')
def hello_world():
    return 'Hello, World!'  # return 'Hello World' in response


@app.route('/students')
def get_students():
    return jsonify(data)  # return student data in response


app.run(host='0.0.0.0', port=8080)


# route variables
@app.route('/students/<id>')
def get_student(id):
    for student in data:
        if student[
                'id'] == id:  # filter out the students without the specified id
            return jsonify(student)


@app.route('/students')
def get_students():
    result = []
    pref = request.args.get('pref')  # get the parameter from url
    if pref:
        for student in data:  # iterate dataset
            if student[
                    'pref'] == pref:  # select only the students with a given meal preference
                result.append(student)  # add match student to the result
        return jsonify(result)  # return filtered set if parameter is supplied
    return jsonify(data)  # return entire dataset if no parameter supplied


#Exercise 2
@app.route('/add/<int:a>/<int:b>')
def add(a, b):
    return f"Result of {a} + {b} = {a + b}"

@app.route('/subtract/<int:a>/<int:b>')
def subtract(a, b):
    return f"Result of {a} - {b} = {a - b}"

@app.route('/multiply/<int:a>/<int:b>')
def multiply(a, b):
    return f"Result of {a} * {b} = {a * b}"

@app.route('/divide/<int:a>/<int:b>')
def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return f"Result of {a} / {b} = {a / b}"

if __name__ == '__main__':
    app.run(debug=True)