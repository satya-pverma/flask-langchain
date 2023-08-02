from flask import Flask, jsonify, request
from ChatBot import *
from ChunkPdf import *
from QuerryPdf import *
app = Flask(__name__)

@app.route('/', methods = [ 'GET'])  
def home():
    return 'Hello from server!'

@app.route('/local', methods = [ 'POST'])
def local():
    if(request.method == 'POST'):
        body = (request.json)['data']
        result = ChatBot(body["querry"])
        return jsonify({'data': result})
    

@app.route('/snbx/chunk', methods = [ 'POST'])
def chunk():
    if(request.method == 'POST'):
        body = (request.json)['data']
        result = ChunkPdf(body["doc_name"])
        return jsonify({'data': result})
    

@app.route('/snbx/querry', methods = [ 'POST'])
def Querry():
    if(request.method == 'POST'):
        body = (request.json)['data']
        result = QuerryPdf(body["querry"], body["chunk"])
        return jsonify({'data': result})
  
  

  
  
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)