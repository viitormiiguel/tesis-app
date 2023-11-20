
from feat.detector import Detector
from feat.data import Fex
from feat.utils.io import get_test_data_path
import matplotlib.pyplot as plt ## for visualization
import os 
import shutil

emoLabels = ['anger', 'disgust', 'fear', 'happiness', 'sadness',  'surprise', 'neutral']

detector = Detector(
    face_model="retinaface",
    landmark_model="mobilefacenet",
    au_model='xgb',
    emotion_model="resmasknet",
    facepose_model="img2pose",
)

path = 'D:\\CG e Real\\Hulk Training Scene  SHE HULK (2022) CLIP 4K\\shehulk\\'

for l in os.listdir(path):
    
    print(l)
    single_face_img_path = os.path.join(path, l)

    single_face_prediction = detector.detect_image(single_face_img_path)

    emotions = single_face_prediction.emotions
    
    # print(emotions)
    
    # List emotions
    lemo = list(emotions.values)
    lemo = list(lemo[0])
    
    maximo = max(lemo)
    getEmo = lemo.index(maximo)
    
    # print(getEmo, emoLabels[getEmo])
    
    src = path + l
    dst = 'D:\\Orgazine Faces\\SheHulk\\' + emoLabels[getEmo] + '\\' + l
    
    shutil.copy(src, dst)
    
    # break