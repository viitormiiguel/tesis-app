
import os 
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
    
    nome = image.split('.')
    nome = nome[0].split('\\')
   
    exec1 = path + image
    exec2 = path + '\\output\\retOpen\\' + nome[1]

    comando = ' -f ' + '"' +  exec1 + '"'

    os.system('"C:\\OpenFace\\FaceLandmarkImg.exe' + comando + ' -out_dir ' + exec2 + '"')

def readFile(image):
    
    nome = image.split('.')
    nome = nome[0].split('\\')
    
    arq = path + 'output\\retOpen\\' + nome[1] + '\\' + nome[1] + '.csv'
                    
    arquivo = pd.read_csv(arq)
    
    valores = arquivo.iloc[:, 676:693]
    
    
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
        'openface': valores.to_json(orient = 'records')
    })
        
    return data, dataOpen

def saveMOngo(ret):
    
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["tesis-app"]
    
    ## Add image data
    mycol = mydb["images"]
    mycol.insert_many(ret[0])
        
    ## Add OpenFace Data Image
    mycol = mydb["openFace"]
    mycol.insert_many(ret[1])        

if __name__ == '__main__':

    path = 'E:\\PythonProjects\\tesis-app\\'
    
    image = 'input\\58-12.jpg'
    
    runOpenFace(image)
    
    r = readFile(image)
    
    saveMOngo(r)
    