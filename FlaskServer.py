from flask import Flask
import flask_cors
from flask_cors import CORS
import ast
app = Flask(__name__)
CORS(app)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/get_paths')
def get_paths():
    toreturn = {}
    with open('oute.txt', 'r') as file:
        lines = [ast.literal_eval(line) for line in file]
        lines.sort(key=lambda x: len(x[0]), reverse=True)
        toreturn = {line[0]: line[1] for line in lines}
    return toreturn



if __name__ == '__main__':
    app.run("0.0.0.0", 5000)