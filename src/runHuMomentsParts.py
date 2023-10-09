
import cv2
import os

import numpy as np
import pandas as pd
import mediapipe as mp
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image

# carregar arquivo csv
def carrega_dado(path_dado):

    return pd.read_csv(path_dado)

# Função para recortar as landmarks especificadas
def crop_landmarks(image, landmarks, landmark_indices):
    
    image_height, image_width, _ = image.shape
    mask = np.zeros((image_height, image_width), dtype=np.uint8)
    
    landmark_points = []
    for index in landmark_indices:
        x, y = int(landmarks[index][0] * image_width), int(landmarks[index][1] * image_height)
        landmark_points.append([x, y])
    
    convex_hull = cv2.convexHull(np.array(landmark_points))
    cv2.fillConvexPoly(mask, convex_hull, 255)
    
    cropped_landmarks = cv2.bitwise_and(image, image, mask=mask)
    
    return cropped_landmarks

def extrai_feature_hu_moments_imagem_cropped(arqs, crop):
    
    # reading the image
    # print('arqs: ',arqs)
    # img = cv2.imread(arqs, cv2.IMREAD_GRAYSCALE)
    # img = cv2.bitwise_not(img)
    img = arqs
    
    colunas = ['hu0_'+crop,'hu1_'+crop,'hu2_'+crop,'hu3_'+crop,'hu4_'+crop,'hu5_'+crop,'hu6_'+crop]
        
    # resizing image
    #resized_img = cv2.resize(img, (48, 48))
        
    # hu moments
    #hu = cv2.HuMoments(cv2.moments(resized_img))
    hu = cv2.HuMoments(cv2.moments(img))
        
    for j in range(0, 7):            
        hu[j] = -1 * np.sign(hu[j]) * np.log10(np.abs(hu[j]))
        
    dtAux = pd.DataFrame(hu.T, columns=colunas)
    #dtAux['path_image'] = arqs
        
    return dtAux

if __name__ == '__main__':
    
    # Inicialize o MediaPipe
    mp_face_mesh = mp.solutions.face_mesh
    mp_drawing = mp.solutions.drawing_utils
    
    # carregar arquivo
    # path_df = 'E:\\Greice\\Doutorado\\Modelos\\UV6.0\\csv\\cropped_face_frontal_1990f_hu_moments.csv'
    path_df = 'E:\\Greice\\Doutorado\\Modelos\\UV6.0\\csv\\cropped_val_face_frontal_4322f_hu_moments.csv'

    df = carrega_dado(path_df)
    dt_total = pd.DataFrame()
    lcropped = []
    
    for i in range(len(df)):
        
        image_path = df['path_image'][i] #.replace('cropped','Openface_Frontal').replace("\\", "\\\\")
        print(image_path)
        
        # Carregue a imagem
        image = cv2.imread(image_path)
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        
        # Carregue o modelo de medição de faces
        with mp_face_mesh.FaceMesh(min_detection_confidence=0.5) as face_mesh:
            results = face_mesh.process(image_rgb)
            
            if results.multi_face_landmarks:
                face_landmarks = results.multi_face_landmarks[0]
                landmarks = {}
                for idx, landmark in enumerate(face_landmarks.landmark):
                    landmarks[idx] = (landmark.x, landmark.y)
                
                # Índices das landmarks a serem recortadas
                landmark_indices = {
                    'testa': [21, 54, 103, 67, 109, 10, 338, 297, 332, 251],
                    'olhos': [21,137,366,251],
                    'nariz': [93,132,58,165, 322,416,435,376,352],
                    'boca': [58, 172, 136, 169, 395, 394, 364, 367, 416],
                    'queixo':[169, 150, 149, 176, 148, 152, 396, 400, 369, 395]
                    }
                dt_aux = pd.DataFrame()
                for land in landmark_indices:
                    print('chave:',land,' valor:',landmark_indices[land])
                    landmark_indices_to_crop = landmark_indices[land]
                    
                    # Chame a função de recorte das landmarks
                    cropped_landmarks_image = crop_landmarks(image, landmarks, landmark_indices_to_crop)
                        
                    # Converter a imagem colorida em uma matriz de escala de cinza
                    #imagem_gray = np.mean(cropped_landmarks_image.copy(), axis=2)
                    imagem_gray = cv2.cvtColor(cropped_landmarks_image.copy(), cv2.COLOR_BGR2GRAY)

                    # extract features
                    aux = extrai_feature_hu_moments_imagem_cropped(imagem_gray, land)
                    if dt_aux.empty:
                        dt_aux = aux
                    else:                
                        dt_aux = pd.concat([dt_aux,aux], axis=1)
                                    
                        
                    # Salve a imagem recortada
                    # cv2.imwrite('caminho/para/salvar/recorte_landmarks.jpg', cropped_landmarks_image)
        
                    # Mostrar ou exibir a imagem recortada (opcional)
                    #plt.imshow(cropped_landmarks_image)
                dt_aux['path_image'] = image_path 
                if dt_total.empty:
                    dt_total = dt_aux
                else:                
                    dt_total = pd.concat([dt_total,dt_aux], axis=0)
                    
    dt_merge = pd.merge(df, dt_total, on='path_image', how='inner')  # Use 'how' para definir o tipo de junção            
    # dt_merge.to_csv('E:\\Greice\\Doutorado\\Modelos\\UV6.0\\csv\\cropped_face_and_parts_frontal_1990f_hu_moments.csv')

    dt_merge.to_csv('E:\\Greice\\Doutorado\\Modelos\\UV6.0\\csv\\cropped_val_face_frontal_and_parts_4322f_hu_moments.csv')