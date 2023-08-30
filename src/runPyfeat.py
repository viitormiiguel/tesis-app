
from feat.detector import Detector
from feat.data import Fex
from feat.utils.io import get_test_data_path
import matplotlib.pyplot as plt ## for visualization
import os 
import pandas as pd

def getHeat(imagem):

    single_face_img_path = os.path.join(path, imagem)

    single_face_prediction = detector.detect_image(single_face_img_path)

    emotions = single_face_prediction.emotions
    
    aus = single_face_prediction.aus

    figs = single_face_prediction.plot_detections(faces='aus-heat', muscles=True, emotion_barplot=False, au_barplot=False, faceboxes=False, add_titles=False)

    # plt.show()
    
    plt.savefig('E:\\PythonProjects\\tesis-app\\data\\output\\retPyfeat\\' + imagem)
    
    return emotions, aus

if __name__ == '__main__':
    
    detector = Detector(
        face_model="retinaface",
        landmark_model="mobilefacenet",
        au_model='xgb',
        emotion_model="resmasknet",
        facepose_model="img2pose",
    )
    
    path = 'E:\\PythonProjects\\tesis-app\\data\\input\\'
    
    img = '064_08.jpg'
    
    ret = getHeat(img)