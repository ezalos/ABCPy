'''Test'''
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    '''Json Hello World'''
    if request.method == 'POST':
        some_json = request.get_json()
        #201 is the response code
        return jsonify({'you sent': some_json}), 201
    else:
        return jsonify({"about" : "Hello World!"})

@app.route('/multi/<int:num>', methods=['GET'])
def get_multiply10(num):
    '''int * 10'''
    return jsonify({'result': num*10})

@app.route('/multi/<num>', methods=['GET'])
def get_multistr(num):
    '''str str'''
    return jsonify({'result': num + ' ' + num})

if __name__ == '__main__':
    app.run(debug=True)
