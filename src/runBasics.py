import os 
import time
import subprocess
import shutil
import csv
import json 
import pymongo
from random_object_id import generate
from bson.objectid import ObjectId
from flask import Flask, request, jsonify

import numpy as np 
import pandas as pd 
from os import path

def getInfos():
    
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    mydb = myclient["tesis-app"]
    
    ## Add image data
    mycol = mydb["images"]
    
    cursor = mycol.find({})
    
    retorno = []
    for document in cursor:
        retorno.append(document)
        
    return retorno
    
if __name__ == '__main__':   
    
    r = getInfos()
    
    print(r)