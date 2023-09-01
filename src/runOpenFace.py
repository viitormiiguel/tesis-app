
import os 
import time
import subprocess
import shutil
import csv
import json 
import pymongo
from random_object_id import generate
from bson.objectid import ObjectId

import numpy as np 
import pandas as pd 
from os import path

def runOpenFace(image):
    
    try:
    
        path = 'E:\\PythonProjects\\tesis-app'
            
        exec1 = path + '\\data\\input\\' + image
        exec2 = path + '\\data\\output\\retOpen\\' + image

        comando = ' -f ' + '"' +  exec1 + '"'

        os.system('"C:\\OpenFace\\FaceLandmarkImg.exe' + comando + ' -out_dir ' + exec2 + '"')
        
        time.sleep(1)
                
        return '## Processo finalizado! ##'
        
    except:        
        return '## Erro ao executar OpenFace ##'
    

def saveData(image):
        
    try:
        
        path = 'E:\\PythonProjects\\tesis-app'
        
        nome = image.split('.')
    
        arq = path + '\\data\\output\\retOpen\\' + image + '\\' + nome[0] + '.csv'
                        
        arquivo = pd.read_csv(arq)
                
        valores = arquivo.iloc[:, 676:693]
        
        land2D = arquivo.iloc[:, 296:432]
            
        land3D = arquivo.iloc[:, 432:636]
        
        idImage = ObjectId(generate())
        idOpen = ObjectId(generate())
        
        data = []    
        data.append({
            'imageId': idImage,
            'personalId': 'teste',
            'image': nome[1],
            'imgeurl': '',
            'type': 'real',
        })
        
        dataOpen = []
        dataOpen.append({
            'openId': idOpen,
            'imageId': idImage,
            'aus': valores.to_json(orient = 'records'),
            'landmarks2D': land2D.to_json(orient = 'records'),
            'landmarks3D': land3D.to_json(orient = 'records'),
        })
                
        time.sleep(1)
        
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["tesis-app"]
        
        ## Add image data
        mycol = mydb["images"]
        mycol.insert_many(data)
            
        ## Add OpenFace Data Image
        mycol = mydb["openFace"]
        mycol.insert_many(dataOpen)   
        
        return '## Processo finalizado! ##'
        
    except:         
        return '## Erro ao salvar no MongoDB ##'

if __name__ == '__main__':

    path = 'E:\\PythonProjects\\tesis-app\\'
    
    image = '064_08.jpg'