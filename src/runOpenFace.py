
import os 
import subprocess
import shutil
import csv
import json 

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
    
    data = {}
    
    data.append({
        'personalId': 'teste',
        'image': nome[1],
        'imgeurl': '',
        'deep3D': False,
        'deca': False,
        'emoca': False
    });
    
    data = valores.to_json(orient = 'records')
    
    print(valores)
    print(data)

def sendReturn():
    
    return 'OK'

if __name__ == '__main__':

    path = 'E:\\PythonProjects\\tesis-app\\'
    
    image = 'input\\58-12.jpg'
    
    # runOpenFace(image)
    
    readFile(image)