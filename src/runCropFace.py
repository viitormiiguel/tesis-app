
import cv2
import os

import numpy as np
import pandas as pd
import mediapipe as mp
import matplotlib.pyplot as plt

from feat import Detector

def cropImage():

    path = './data/input/'

    detector = Detector(
        face_model="retinaface",
        landmark_model="mobilefacenet",
        au_model='xgb',
        emotion_model="resmasknet",
        facepose_model="img2pose",
    )

    single_face_img_path = os.path.join(path, "50-12.jpg")

    single_face_prediction = detector.detect_image(single_face_img_path)

    # Show results
    print(single_face_prediction.facebox)

    lista = list(single_face_prediction.facebox.values)

    # x = int(lista[0][0]) - 30 
    # y = int(lista[0][1]) - 70
    # h = int(lista[0][3]) + 100
    # w = int(lista[0][2]) + 50

    x = int(lista[0][0]) 
    y = int(lista[0][1])
    h = int(lista[0][3])
    w = int(lista[0][2])

    img = cv2.imread(path + "50-12.jpg")
    
    crop_img = img[y:y+h, x:x+w]
    
    cv2.imshow("cropped", crop_img)
    cv2.waitKey(0)


if __name__ == "__main__": 

    cropImage()