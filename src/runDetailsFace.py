
import dlib
import cv2
import os
import imutils

import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

from PIL import Image, ImageDraw


# path = 'E:/PythonProjects/Deep3DFaceReconstruction/imgs/posed/fei/'
# path = 'C:/Users/vitor/OneDrive - PUCRS - BR/Dataset 3D Faces/Dataset_DDataset 3D Faces/Dataset_Deep3D/posed/men/ep3D/posed/men/'

# CHEEK_IDXS = OrderedDict(
#     [
#         ("left_cheek", (1,2,3,4,5,48,49,31)),
#         ("right_cheek", (11,12,13,14,15,35,53,54)),
#         ("left_eye", (36,37,38,39,40,41)),
#         ("right_eye", (42, 43,44,45,46,47))
#     ]
# )

CHEEK_IDXS = OrderedDict(
    [
        ("all", (0 , 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 16, 28)),
    ]
)


detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("./model/shape_predictor_68_face_landmarks.dat")

img = cv2.imread('./img/' + '029_08_mesh.png')
img = imutils.resize(img, width=600)

overlay = img.copy()
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

detections = detector(gray, 0)
for k,d in enumerate(detections):
    
    shape = predictor(gray, d)
    for (_, name) in enumerate(CHEEK_IDXS.keys()):
        
        pts = np.zeros((len(CHEEK_IDXS[name]), 2), np.int32) 
        
        for i,j in enumerate(CHEEK_IDXS[name]): 
            pts[i] = [shape.part(j).x, shape.part(j).y]

        pts = pts.reshape((-1,1,2))
        cv2.polylines(overlay,[pts],True,(0,255,0),thickness = 2)
    
    cv2.imshow("Image", overlay)
    cv2.imwrite('teste.png', overlay)
    cv2.waitKey(0)
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break

cv2.destroyAllWindows()

image = Image.open('./teste.png')
width, height = image.size
center = (int(0.5 * width), int(0.5 * height))
yellow = (255, 255, 0, 255)
ImageDraw.floodfill(image, xy=center, value=yellow)
image.save('teste1.png')