'''Test'''
from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    '''Json Hello World'''
    return jsonify({"about" : "Hello World!"})

if __name__ == '__main__':
    app.run(debug=True)
