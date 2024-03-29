
import dlib
import cv2
import os
import numpy as np
import matplotlib.pyplot as plt

from imutils import face_utils
from PIL import Image

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('./model/shape_predictor_68_face_landmarks.dat')

def createTxtDeep(imagesp):
    
    subpastas = os.listdir(imagesp)
        
    for p in subpastas:

        pimg = imagesp + p
        
        img = cv2.imread(pimg)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        rects = detector(gray, 0)
        
        if len(rects) > 0:
    
            for rect in rects:

                x = rect.left()
                y = rect.top()
                w = rect.right()
                h = rect.bottom()

            shape = predictor(gray, rect)
            shape_np = face_utils.shape_to_np(shape).tolist()
            left_eye = midpoint(shape_np[36], shape_np[39])
            right_eye = midpoint(shape_np[42], shape_np[45])
            features = [left_eye, right_eye, shape_np[33], shape_np[48], shape_np[54]]   

            with open(imagesp + "/" + p.split('.')[0] + ".txt", "a") as f:
                for i in features:
                    print(str(i[0]) + ' ' + str(i[1]), file=f)   
                    
def midpoint(p1, p2):
    
    coords = (p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2
	
    return [int(x) for x in coords]

if __name__ == '__main__':
    
    path = 'E:/PythonProjects/tesis-view/images/pro/'
    
    createTxtDeep(path)