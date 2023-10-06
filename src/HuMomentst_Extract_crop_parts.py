import cv2
import numpy as np
import os
import pandas as pd
import mediapipe as mp
from PIL import Image
import matplotlib.pyplot as plt
import seaborn as sns


# lista arquivos
def listFile(path):
    lista = []
    for p, _, files in os.walk(os.path.abspath(path)):
        for file in files:
            lista.append(os.path.join(p, file))  
    return lista

# carregar arquivo csv
def carrega_dado(path_dado):
    return pd.read_csv(path_dado)

# Função para desenhar os landmarks na imagem
def draw_landmarks(image, landmarks):
    for landmark in landmarks:
        for point in landmark.landmark:
            x, y = int(point.x * image.shape[1]), int(point.y * image.shape[0])
            cv2.circle(image, (x, y), 2, (0, 255, 0), -1)

# Função para recortar o contorno da face
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


def extrai_feature_hu_moments_imagem(arqs):
    # reading the image
    print('arqs: ',arqs)
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

####################################################################


# Extract  dados

#path_cropped = 'E:\\Greice\\Doutorado\\Modelos\\UV6.0\\cropped\\'
path_cropped = 'E:\\Greice\\Doutorado\\Modelos\\UV6.0\\cropped_val\\'
#path_image = 'E:\\Greice\\Doutorado\\Modelos\\UV6.0\\Openface_QtdFrames\\30\\'
#path_image = 'E:\\Greice\\Doutorado\\Modelos\\UV6.0\\Openface_Frontal\\30\\'
path_image = 'E:\\Greice\\Doutorado\\Modelos\\UV6.0\\Openface\\48\\'


lista_image = listFile(path_image)
lista_cropped = [ arquivo for arquivo in lista_image if arquivo.endswith(".bmp") ]


for i in range(len(lista_cropped)):
    
    nova_imagem = lista_cropped[i].split('\\')[-1]
    diretorio_imagem = lista_cropped[i].split('\\')[-3]
    
    image = cv2.imread(lista_cropped[i])
    
    # Inicializar o MediaPipe
    mp_face_mesh = mp.solutions.face_mesh
    face_mesh = mp_face_mesh.FaceMesh()
    
    # Converter a imagem para RGB (MediaPipe requer imagens em RGB)
    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    # Detectar os landmarks faciais na imagem
    results = face_mesh.process(image_rgb)
    landmarks = results.multi_face_landmarks
    
    # Criar uma cópia da imagem original
    image_with_landmarks = image.copy()
    
    try:
        # Desenhar os landmarks na imagem original
        draw_landmarks(image_with_landmarks, landmarks)    
        
        # Recortar o contorno da face (Exemplo de implementação - use a sua própria lógica)
        cropped_face = crop_face(image, landmarks)
        
        cropped_face = cv2.cvtColor(cropped_face, cv2.COLOR_BGR2RGB)
        
        # Converta o array NumPy em um objeto Image
        imagem_pillow = Image.fromarray(cropped_face)
        
        if not os.path.exists(path_cropped+'\\'+diretorio_imagem):
        # Crie a pasta e seus diretórios intermediários
            os.makedirs(path_cropped+'\\'+diretorio_imagem)
        
        # Agora você pode salvar a imagem usando o objeto Image
        imagem_pillow.save(path_cropped+'\\'+diretorio_imagem+'\\'+nova_imagem)
    except:
        None        
#

# Gerando arquivo

dic = {1:41.18,2:91.6,3:68.91,4:37.82,5:26.89,6:88.24,7:84.03,8:71.43,9:63.87,10:92.44,
       11:35.29,12:91.6,13:94.96,14:81.51,15:52.1,16:89.08,17:73.11,18:85.71,19:24.37,20:67.23,
       21:77.31,22:79.83,23:44.00,24:30.00,25:72.00,26:75.00,27:51.00,28:44.00,29:23.00,30:44.00,
       31:13.00,32:56.00,33:72.00,34:0.00,35:30.00,36:0.00,37:52.00,38:54.00,39:51.00,40:0.00,
       41:52.00,42:64.00,43:64.00,44:0.00,48:0.00,49:57.00,50:85.00,51:0.00,52:0.00,53:39.00,54:93.00,55:97.00,56:30.00}

char = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,48,49,50,51,52,53,54,55,56])
comfort = np.array([41.18,91.6,68.91,37.82,26.89,88.24,84.03,71.43,63.87,92.44,35.29,91.6,94.96,81.51,52.1,89.08,73.11,85.71,24.37,67.23,77.31,79.83,
44.00,30.00,72.00,75.00,51.00,44.00,23.00,44.00,13.00,56.00,72.00,0.00,30.00,0.00,52.00,54.00,51.00,0.00,52.00,64.00,64.00,0.00,0.00,57.00,85.00,0.00,0.00,39.00,93.00,97.00,30.00
])

character = pd.DataFrame(char, columns=['character'])
comf = pd.DataFrame(comfort, columns=['comfort'])
a = character.join(comf)

#path_cropped = 'E:\\Greice\\Doutorado\\Modelos\\UV6.0\\cropped\\'
path_cropped = 'E:\\Greice\\Doutorado\\Modelos\\UV6.0\\cropped_val\\'
lista_image = listFile(path_cropped)

dt = pd.DataFrame()
for i in range(len(lista_image)):
    aux = extrai_feature_hu_moments_imagem(lista_image[i])
    if dt.empty:
        dt = aux
    else:
        dt = pd.concat([dt,aux], axis=0)


dt.reset_index(drop=True, inplace=True)
dt['character'] = [ dt['path_image'][i].split('\\')[-2] for i in range(len(dt)) ]
dt['comfort'] = [ a[a['character']==int(c)]['comfort'].values[0] for c in dt['character'] ]

dt['UV'] = 0
dt['UV'] = [ 1 if c<= 50 else 0 for c in dt['comfort'] ]
dt['UV'].value_counts()

dt = dt[['path_image',
       'character', 'comfort','UV', 'hu0', 'hu1', 'hu2', 'hu3', 'hu4', 'hu5', 'hu6']]


dt.to_csv('E:\\Greice\\Doutorado\\Modelos\\UV6.0\\csv\\cropped_val_face_frontal_4322f_hu_moments.csv')



plt.figure(figsize=(10,6))
sns.countplot(x='character', data=dt)
plt.xlabel('Personagens')
plt.ylabel('Quantidade');


plt.figure(figsize=(10,6))
sns.countplot(x='UV', data=dt)
plt.xlabel('Conforto (0) x Desconforto (1)')
plt.ylabel('Quantidade');


###################################################################################

################# CROP DE PARTES DA FACE ###########################

import cv2
import mediapipe as mp

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
