
import dlib
import cv2
import os
import imutils

import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

from PIL import Image, ImageDraw

def drawRegiona(imagem, valores, label):

    nome = imagem.split('.')
    
    listas = ['eye', 'month', 'nose', 'queixo']

    CHEEK_IDXS = OrderedDict(
        [
            valores
        ]
    )

    detector    = dlib.get_frontal_face_detector()
    predictor   = dlib.shape_predictor("./model/shape_predictor_68_face_landmarks.dat")

    img = cv2.imread('./img/' + imagem)
    img = imutils.resize(img, width=600)

    overlay = img.copy()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    mask = np.zeros_like(img, np.uint8)
    # mask = np.zeros((img.shape[0], img.shape[1]))

    detections = detector(gray, 0)
    for k,d in enumerate(detections):
        
        shape = predictor(gray, d)
        for (_, name) in enumerate(CHEEK_IDXS.keys()):
            
            pts = np.zeros((len(CHEEK_IDXS[name]), 2), np.int32) 
            
            for i,j in enumerate(CHEEK_IDXS[name]): 
                pts[i] = [shape.part(j).x, shape.part(j).y]

            # pts = pts.reshape((-1,1,2))
            
            # cv2.polylines(overlay,[pts],True,(246,243,243),thickness = 2)            
            # cv2.fillPoly(overlay, pts=[pts], color=(180,0,0))
            
            
            # Create output image (untranslated)
            outClean = img.copy()
            
            # Create mask that defines the polygon of points
            # Red
            cv2.fillConvexPoly(mask, pts, (0, 0, 255))
            # Blue
            # cv2.fillConvexPoly(mask, pts, (255, 51, 51))
            
            alpha = 0.7
            mascara = mask.astype(bool)
            outClean[mascara] = cv2.addWeighted(img, alpha, mask, 1 - alpha, 0)[mascara]
            
            mask = mask > 0 # To convert to Boolean
            
            out = np.zeros_like(img)
            out[mask] = img[mask]
            
            # Find centroid of polygon
            (meanx, meany) = pts.mean(axis=0)

            # Find centre of image
            (cenx, ceny) = (img.shape[1]/2, img.shape[0]/2)
            
            # Make integer coordinates for each of the above
            (meanx, meany, cenx, ceny) = np.floor([meanx, meany, cenx, ceny]).astype(np.int32)

            # Calculate final offset to translate source pixels to centre of image
            (offsetx, offsety) = (-meanx + cenx, -meany + ceny)

            # Define remapping coordinates
            (mx, my) = np.meshgrid(np.arange(img.shape[1]), np.arange(img.shape[0]))
            ox = (mx - offsetx).astype(np.float32)
            oy = (my - offsety).astype(np.float32)

            # Translate the image to centre
            out_translate = cv2.remap(out, ox, oy, cv2.INTER_LINEAR)

            # Determine top left and bottom right of translated image
            # topleft = pts.min(axis=0) + [offsetx, offsety]
            # bottomright = pts.max(axis=0) + [offsetx, offsety]
                        
            # cv2.imshow('Output Image', out_translate)
            # cv2.imshow('Output', outClean)
            
            cv2.imwrite('./img/' + nome[0] + '_' + str(listas[label]) + '_detail.jpg', outClean)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
                    
        # cv2.imshow("Image", overlay)


if __name__ == '__main__':

    parts = [
        ("eyes", (21, 20, 19, 18, 17, 0, 1, 29, 15, 16, 26, 25, 24, 23, 22)),
        ("month", (3, 4, 5, 11, 12, 13, 35, 34, 33, 32, 31)),
        ("nose", (3, 13, 14, 15, 28, 1, 2)),
        ("queixo", (4, 5, 6, 7, 8, 9, 10, 11, 12, 54, 55, 56, 57, 58, 59, 60, 48))
    ]

    lista = os.listdir('./img/')
    
    for i, j in enumerate(parts):

        for l in lista:

            if 'detail' not in l:

                drawRegiona(l, j, i)
             
        #     break
                
        # break