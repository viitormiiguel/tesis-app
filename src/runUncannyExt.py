
import cv2
import os
import numpy as np
import pandas as pd
import mediapipe as mp
import matplotlib.pyplot as plt
import seaborn as sns

from PIL import Image

## Lista arquivos
def listFile(path):
    
    lista = []    
    for p, _, files in os.walk(os.path.abspath(path)):
        for file in files:
            lista.append(os.path.join(p, file))  
    
    return lista

## Função para desenhar os landmarks na imagem
def draw_landmarks(image, landmarks):
    
    for landmark in landmarks:
    
        for point in landmark.landmark:
            x, y = int(point.x * image.shape[1]), int(point.y * image.shape[0])
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)

## Função para recortar o contorno da face
def crop_face(image, landmarks):
    
    image_height, image_width, _ = image.shape
    mask = np.zeros((image_height, image_width), dtype=np.uint8)
    landmark_points = []
    
    for landmark in landmarks:
        for point in landmark.landmark:
            x, y = int(point.x * image_width), int(point.y * image_height)
            landmark_points.append([x, y])
    
    convex_hull = cv2.convexHull(np.array(landmark_points))
    cv2.fillConvexPoly(mask, convex_hull, 255)
    face_image = cv2.bitwise_and(image, image, mask=mask)
    
    return face_image

## Extrair features Hu Moments
def extrai_feature_hu_moments_imagem(arqs):
    
    # reading the image
    # print('arqs: ',arqs)
    img = cv2.imread(arqs, cv2.IMREAD_GRAYSCALE)
    img = cv2.bitwise_not(img)
        
    # resizing image
    #resized_img = cv2.resize(img, (48, 48))
        
    # hu moments
    #hu = cv2.HuMoments(cv2.moments(resized_img))
    hu = cv2.HuMoments(cv2.moments(img))
        
    for j in range(0, 7):            
        hu[j] = -1 * np.sign(hu[j]) * np.log10(np.abs(hu[j]))
        
    dtAux = pd.DataFrame(hu.T, columns=['hu0','hu1','hu2','hu3','hu4','hu5','hu6'])
    dtAux['path_image'] = arqs
        
    return dtAux

if __name__ == '__main__':
    
    ## Inicialize o MediaPipe
    mp_face_mesh = mp.solutions.face_mesh
    mp_drawing = mp.solutions.drawing_utils
    
    ## Images para extração de features
    path_image = './model/images/test/'
    
    lista_image     = listFile(path_image)    
    lista_cropped   = [ arquivo for arquivo in lista_image if arquivo.endswith(".png") or arquivo.endswith(".bmp") ]
    
    for i in range(len(lista_cropped)):
        
        if '\\' in lista_cropped[i]:        
            nova_imagem = lista_cropped[i].split('\\')[-1] 
            diretorio_imagem = lista_cropped[i].split('\\')[-3]        
        else:        
            nova_imagem = lista_cropped[i].split('/')[-1]
            diretorio_imagem = lista_cropped[i].split('/')[-3]
            
        image = cv2.imread(lista_cropped[i])
        
        ## Inicializar o MediaPipe
        mp_face_mesh = mp.solutions.face_mesh
        face_mesh = mp_face_mesh.FaceMesh()
        
        ## Converter a imagem para RGB (MediaPipe requer imagens em RGB)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        ## Detectar os landmarks faciais na imagem
        results = face_mesh.process(image_rgb)
        landmarks = results.multi_face_landmarks
        
        ## Criar uma cópia da imagem original
        image_with_landmarks = image.copy()
        
        try:
            
            # Desenhar os landmarks na imagem original
            draw_landmarks(image_with_landmarks, landmarks)    
            
            # Recortar o contorno da face (Exemplo de implementação - use a sua própria lógica)
            cropped_face = crop_face(image, landmarks)
            
            cropped_face = cv2.cvtColor(cropped_face, cv2.COLOR_BGR2RGB)
            
            # Converta o array NumPy em um objeto Image
            imagem_pillow = Image.fromarray(cropped_face)
            
            if not os.path.exists(path_image+'/'+diretorio_imagem):
            # Crie a pasta e seus diretórios intermediários
                os.makedirs(path_image+'/'+diretorio_imagem)
            
            # Agora você pode salvar a imagem usando o objeto Image
            imagem_pillow.save(path_image+'/'+diretorio_imagem+'/'+nova_imagem)
            
        except:
            None 
            
    dic = {
        1:41.18,2:91.6,3:68.91,4:37.82,5:26.89,6:88.24,7:84.03,8:71.43,9:63.87,10:92.44,
        11:35.29,12:91.6,13:94.96,14:81.51,15:52.1,16:89.08,17:73.11,18:85.71,19:24.37,20:67.23,
        21:77.31,22:79.83,23:44.00,24:30.00,25:72.00,26:75.00,27:51.00,28:44.00,29:23.00,30:44.00,
        31:13.00,32:56.00,33:72.00,34:0.00,35:30.00,36:0.00,37:52.00,38:54.00,39:51.00,40:0.00,
        41:52.00,42:64.00,43:64.00,44:0.00,48:0.00,49:57.00,50:85.00,51:0.00,52:0.00,53:39.00,54:93.00,55:97.00,56:30.00
    }
    
    comfort = np.array(
        [
            41.18,91.6,68.91,37.82,26.89,88.24,84.03,71.43,63.87,92.44,35.29,91.6,94.96,81.51,52.1,89.08,73.11,85.71,
            24.37,67.23,77.31,79.83,44.00,30.00,72.00, 75.00,51.00,44.00,23.00,44.00,13.00,56.00,72.00,0.00,30.00,0.00,
            52.00,54.00,51.00,0.00,52.00,64.00,64.00,0.00,0.00,57.00,85.00,0.00,0.00,39.00,93.00,97.00,30.00
        ]
    )
    
    path_cropped    = './model/images/test/test/'
    lista_image     = listFile(path_cropped)
    
    dt = pd.DataFrame()
    for i in range(len(lista_image)):
        
        aux = extrai_feature_hu_moments_imagem(lista_image[i])
        
        if dt.empty: dt = aux
        else: dt = pd.concat([dt,aux], axis=0)
        
    dt.reset_index(drop=True, inplace=True)
    
    dt = dt[['path_image', 'hu0', 'hu1', 'hu2', 'hu3', 'hu4', 'hu5', 'hu6']]

    dt.to_csv('./model/images/test/hu_face_toda_hu_moments.csv')