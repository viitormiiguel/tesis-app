
import time
import os
import json
import pymongo
from flask import Flask, request, jsonify

from src.runOpenFace import runOpenFace
from src.runOpenFace import saveData
from src.runPyfeat import getHeat
from src.runBasics import getInfos

app = Flask(__name__)

## Create data from new images (OpenFace, PyFeat and Heatmap)
@app.route('/api/createData', methods=['POST'])
def createData():
    
    request_body = request.get_json()
    
    data = {'file': request_body['file']}
    
    try:
        
        r = runOpenFace(request_body['file'])
                
        s = saveData(request_body['file'])
        
        t = getHeat(request_body['file'])
            
        return '## Dados salvos com sucesso! ##'
        
    except:
        return '## Erro ao executar OpenFace ##'
    
    
## GET (Get image list)
@app.route('/api/getImageList/', methods=['GET'])
def getImageList():
    
    try:        
        
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["tesis-app"]
        
        ## Add image data
        mycol = mydb["openFace"]
        
        cursor = mycol.find_one({}, {'_id': '64f24ba35ebb3f04096f967a'})   
   
        return jsonify(cursor)
        
    except:
        return '## Erro ao listar imagens ##'
    
## GET (Get image)
@app.route('/getImage', methods=['GET'])
def getImage():
    
    try:        
        print('teste')        
    except:
        return '## Erro ao executar OpenFace ##'
 
## Save Image   
@app.route('/saveImage', method=['POST'])
def saveImage():
    
    try:        
        print('teste')        
    except:
        return '## Erro ao executar OpenFace ##'
    

if __name__ == '__main__':
    
    app.run(host='0.0.0.0', port=105)