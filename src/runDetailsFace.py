
import dlib
import cv2
import os
import imutils

import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

from PIL import Image, ImageDraw

def drawRegiona(imagem):

    nome = imagem.split('.')

    CHEEK_IDXS = OrderedDict(
        [
            ("all", (21, 20, 19, 18, 17, 0, 1, 29, 15, 16, 26, 25, 24, 23, 22)),
        ]
    )

    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor("./model/shape_predictor_68_face_landmarks.dat")

    img = cv2.imread('./img/' + imagem)
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

            
            cv2.polylines(overlay,[pts],True,(246,243,243),thickness = 2)
            # cv2.fillPoly(overlay, pts=[pts], color=(246,243,243))
        
        # cv2.imshow("Image", overlay)
        cv2.imwrite('./img/' + nome[0] + '_detail.jpg', overlay)
    #     cv2.waitKey(0)
    #     if cv2.waitKey(1) & 0xFF == ord('q'): 
    #         break

    # cv2.destroyAllWindows()

if __name__ == '__main__':

    lista = os.listdir('./img/')

    for l in lista:

        if 'detail' not in l:

            drawRegiona(l)