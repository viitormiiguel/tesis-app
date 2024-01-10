
import dlib
import cv2
import os
import imutils
import pandas as pd

import numpy as np
import matplotlib.pyplot as plt
from collections import OrderedDict

from PIL import Image, ImageDraw

def drawRegiona(imagem, valores, intensidade):

    nome = imagem.split('.')
    
    listas = ['eye', 'month', 'nose', 'queixo']
    
    img = cv2.imread('./img/cg/' + imagem)
    # img = imutils.resize(img, width=600)

    # Create output image (untranslated)
    if '_detail' in imagem:
        imagedet = img = cv2.imread('./img/' + nome[0] + '_detail.jpg')
        imagedet = imutils.resize(imagedet, width=600)
        outClean = imagedet.copy()
    else:
        outClean = img.copy()        
    
    for m, n in enumerate(valores):

        CHEEK_IDXS = OrderedDict([n])

        detector    = dlib.get_frontal_face_detector()
        predictor   = dlib.shape_predictor("./model/shape_predictor_68_face_landmarks.dat")        

        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        mask = np.zeros_like(img, np.uint8)

        detections = detector(gray, 0)
        for k,d in enumerate(detections):
            
            shape = predictor(gray, d)
            for (_, name) in enumerate(CHEEK_IDXS.keys()):
                
                pts = np.zeros((len(CHEEK_IDXS[name]), 2), np.int32) 
                
                for i,j in enumerate(CHEEK_IDXS[name]): 
                    pts[i] = [shape.part(j).x, shape.part(j).y]            
                
                # Create mask that defines the polygon of points
                if intensidade[m] == -1:
                    cv2.fillPoly(mask, [pts], (0, 0, 255))
                if intensidade[m] == 1:
                    cv2.fillPoly(mask, [pts], (255, 51, 51))
                # White
                # cv2.fillPoly(mask, [pts], (255, 255, 255))
                
                alpha = 0.7
                mascara = mask.astype(bool)
                outClean[mascara] = cv2.addWeighted(img, alpha, mask, 1 - alpha, 0)[mascara]
                
                cv2.imwrite('./img/annotated/' + nome[0] + '_detail.jpg', outClean)
                
        # break
        
def diffsOpen(image):
    
    path = './data/openface/'
    
    ## Real                
    arq     = path + 'real/' + image + '.csv'                    
    arquivo = pd.read_csv(arq)            
    valReal = arquivo.iloc[:, 676:693]
    
    ## CG                
    arq     = path + 'cg/' + image + '_mesh.csv'                    
    arquivo = pd.read_csv(arq)            
    valCg   = arquivo.iloc[:, 676:693]
    
    val1 = valReal.values
    val2 = valCg.values
    
    difs = []
    for i, j in enumerate(val1[0]):
        
        if int(j) > int(val2[0][i]):
            print(j, val2[0][i], "CG Menor")
            difs.append('menor')
            
        if int(j) < int(val2[0][i]):
            print(j, val2[0][i], "CG Maior")
            difs.append('maior')
            
        if int(j) == int(val2[0][i]):
            print(j, val2[0][i], "IGUAL")
            difs.append('igual')
    
    return difs

if __name__ == '__main__':

    parts = [
        ("eyes", (21, 20, 19, 18, 17, 0, 1, 29, 15, 16, 26, 25, 24, 23, 22)),
        ("month", (3, 4, 5, 11, 12, 13, 35, 34, 33, 32, 31)),
        ("nose", (3, 13, 14, 15, 28, 1, 2)),
        ("queixo", (4, 5, 6, 7, 8, 9, 10, 11, 12, 54, 55, 56, 57, 58, 59, 60, 48))
    ]
        
    # r = diffsOpen('021_08')
    
    # print(r)
    
    # exit()
    
    lista = os.listdir('./img/cg/')
    
    for l in lista:

        drawRegiona(l, [parts[0], parts[1]], [-1, 1])