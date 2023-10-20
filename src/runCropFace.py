
import cv2
import os

import numpy as np
import pandas as pd
import mediapipe as mp
import matplotlib.pyplot as plt

import dlib
import argparse

from feat import Detector

ap = argparse.ArgumentParser()
# ap.add_argument('-i', '--image', required=True, help='path to image file')
ap.add_argument('-w', '--weights', default='./model/mmod_human_face_detector.dat', help='path to weights file')

args = ap.parse_args()

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

def detectFace(teste):
    
    path = './data/input/'
    
    face_cascade = cv2.CascadeClassifier('./model/haarcascade_frontalface_default.xml') # pylint: disable=no-member
    
    imagem  = cv2.imread(path + teste + '.jpg')    
    gray    = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY) # pylint: disable=no-member
    faces   = face_cascade.detectMultiScale(gray, 1.1, 4, minSize=(100, 100))
    
    face_crop = []
    for (x, y, w, h) in faces: 
        
        # cv2.rectangle(imagem, (x,y), (x+w, y+h), (255, 0, 0), 2) # pylint: disable=no-member
                
        img_face = path + teste + "_crop_2.jpg"
        
        # x = x - 30 
        # y = y - 180
        # h = h + 300
        # w = w + 50

        cv2.imwrite(img_face, imagem[y:y+h, x:x+w]) # pylint: disable=no-member
    

if __name__ == "__main__": 

    # cropImage()
    
    detectFace('58-12')