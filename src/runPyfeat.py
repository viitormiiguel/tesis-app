
from feat.detector import Detector
from feat.data import Fex
from feat.utils.io import get_test_data_path
import matplotlib.pyplot as plt ## for visualization
import os 
import pandas as pd
import json 
import pymongo
from random_object_id import generate
from bson.objectid import ObjectId
import time

def getHeat(imagem):
    
    try:
        
        detector = Detector(
            face_model="retinaface",
            landmark_model="mobilefacenet",
            au_model='xgb',
            emotion_model="resmasknet",
            facepose_model="img2pose",
        )
        
        path = 'E:\\PythonProjects\\tesis-app'
        
        path_img = path + '\\data\\output\\retDeep\\'

        single_face_img_path = os.path.join(path_img, imagem)

        single_face_prediction = detector.detect_image(single_face_img_path)

        emotions = single_face_prediction.emotions
            
        aus = single_face_prediction.aus

        figs = single_face_prediction.plot_detections(faces='aus-heat', muscles=True, emotion_barplot=False, au_barplot=False, faceboxes=False, add_titles=False)
        
        plt.savefig(path + '\\data\\output\\retPyfeat\\' + imagem)
        
        idPyfeat = ObjectId(generate())
        
        data = []
        data.append({
            'pyFeatId': idPyfeat,
            'imageId': '',
            'emotions': emotions.to_json(orient='records'),
            'aus': aus.to_json(orient='records'),
        })
        
        # time.sleep(1)
        
        # myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        # mydb = myclient["tesis-app"]
        
        # ## Add image data
        # mycol = mydb["pyFeat"]
        # mycol.insert_many(data)
        
    except: 
        return '## Erro ao salvar no MongoDB ##'
    
if __name__ == '__main__':    
    
    img = '012_08_mesh.png'
    
    ret = getHeat(img)