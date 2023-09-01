
import time
import os

from flask import Flask, request

from src.runOpenFace import runOpenFace
from src.runOpenFace import saveData

app = Flask(__name__)

## POST
@app.route('/createData', methods=['POST'])
def createData():
    
    request_body = request.get_json()
    
    data = {'file': request_body['file']}
    
    try:
        
        r = runOpenFace(request_body['file'])
                
        s = saveData(request_body['file'])
            
        return '## Dados salvos com sucesso! ##'
        
    except:
        return '## Erro ao executar OpenFace ##'
    
    
## GET 
@app.route('/getData', methods=['GET'])
def getData():
    
    try:
        
        print('teste')
        
    except:
        return '## Erro ao executar OpenFace ##'

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=105)