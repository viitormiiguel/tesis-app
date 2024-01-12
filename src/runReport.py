
import os
import csv
import pandas as pd

from fpdf import FPDF

def geraPdf():
    
    ret = getValores()
    # for r in ret:
    #     print(r)
    
    pathReal = 'E:/PythonProjects/tesis-view/images/'
    pathOutput = 'E:/PythonProjects/tesis-view/output/'
    
    class PDF(FPDF):
                
        def capa(self):
            
            pdf.add_page()
            self.image('./resource/capa_report.png', x = 0, y = 0, w = 220, h=299)

            self.ln(6)
            self.set_font("Poppins", "", 20)

            self.set_y(130)
            
            self.set_text_color(0, 113, 192)
            self.set_font("Poppins", "", 50)
            self.ln(5)
            self.cell(63, 10,"Facial", 0, 1, "R")
            self.ln(5)
            self.cell(107, 14,"Expression", 0, 1, "R")
            self.set_text_color(104, 104, 104)
            self.ln(5)
            self.cell(87, 14,"Analysis", 0, 1, "R")
            
            self.set_text_color(0, 0, 0)
            self.set_font("Poppins", "", 20)
            self.ln(5)
            self.set_x(19)
            # self.cell(120, 22, nome, 0, 1, 'L')
            
            self.set_text_color(0, 0, 0)
            self.set_font("Poppins", "", 13)
            self.set_y(180)
            self.set_x(19)
            # self.cell(120, 22, data, 0, 1, 'L')
            
            self.ln(5)   
            
        def header(self):
            if self.page_no()!=1:
                pdf.set_text_color(0, 0, 0)
                self.set_font("Poppins", "", 14)
                self.set_x(-10)
                self.set_x(10)
                self.cell(0, 10, str(self.page_no()-1), 0, 0, "R")
                
        def footer(self):
            if self.page_no()!=1:
                self.set_xy(0,-8)
                # self.image('./resource/header_capa.png')
            
        def pagina(self, label):
            self.add_page()
            self.set_font("Poppins", "", 20)
            self.set_fill_color(236, 236, 236)
            self.set_xy(20,19)
            pdf.set_text_color(0, 0, 0) 
            self.ln(4)

        def final(self):
            self.add_page()
            # self.image('./fontes/barra_v.png', x = 73, y = 20, w = 3.5, h = 8)
            self.set_font("Poppins", "", 22)
            pdf.set_text_color(0, 0, 0)
            self.set_xy(75,21)
            self.cell(0, 6,'agradecemos', 0, 1, 'L')
            # self.image('./fontes/logo+selo.png', x = 52.5, y =56,w=100)
            # self.image('fontes/dicas.png',15,100,w=180)
            
    # Cria pdf com dados
    pdf = PDF()
    
    pdf.add_font('Poppins','','./fontes/Poppins-Bold.ttf',uni=True)
    pdf.alias_nb_pages()
    pdf.capa()
    
    ## Initialize with the photos of real faces
    for i, v in enumerate(ret[1]):
    
        ######################################### Apresentacao ##################################################
        pdf.pagina('Olá time')
        pdf.image('./resource/header-faces.png', x = 0, y = 0, w = 260, h = 26)
        pdf.set_fill_color(236, 236, 236)
        pdf.set_xy(0,0)
        pdf.set_text_color(255, 255, 255)
        pdf.set_x(20)
        pdf.cell(260, 28,'Facial Analysis', 0, 1, 'L')

        ######################################### CAPTURE 1 ##################################################
        pdf.set_font("Poppins", "", 12)
        pdf.set_text_color(0, 0, 0)
        pdf.set_xy(20, 38)
        pdf.set_text_color(0, 113, 192)
        pdf.multi_cell(170,5,"Capture " + str(i+1) + " (Real Face)", 0,'L')
        pdf.set_font("Poppins", "", 10)
        
        pdf.image(str(v), x=22, y=50, w=28)
        
        pdf.set_text_color(0, 0, 0)    
        pdf.set_xy(60, 38)
        pdf.multi_cell(170, 30,"Facial Information:", 0,'L')
        
        pdf.set_font("Poppins", "", 8)
        pdf.set_xy(60, 60)
        pdf.multi_cell(170,5,"Emotion - HAPPINESS", 0,'L')
        pdf.set_xy(60, 68)
        pdf.multi_cell(170,5,"Confident - 95%", 0,'L')
        pdf.set_xy(60, 76)
        pdf.multi_cell(170,5,"Emotion's Intensity - 76%", 0,'L')
        pdf.set_xy(60, 84)
        pdf.multi_cell(170,5,"AUs Intensity - 76%", 0,'L')
        
        pdf.set_font("Poppins", "", 10)
        pdf.set_xy(115, 38)
        pdf.multi_cell(170, 30,"Facial Action Units Intensity:", 0,'L')
        
        pdf.set_font("Poppins", "", 8)
        pdf.set_xy(115, 60)
        pdf.multi_cell(170,5,"AU01 - " + str(ret[5][i][0]), 0,'L')
        pdf.set_xy(115, 65)
        pdf.multi_cell(170,5,"AU02 - " + str(ret[5][i][1]), 0,'L')
        pdf.set_xy(115, 70)
        pdf.multi_cell(170,5,"AU04 - " + str(ret[5][i][2]), 0,'L')
        pdf.set_xy(115, 75)
        pdf.multi_cell(170,5,"AU05 - " + str(ret[5][i][3]), 0,'L')
        pdf.set_xy(115, 80)
        pdf.multi_cell(170,5,"AU06 - " + str(ret[5][i][4]), 0,'L')
        pdf.set_xy(115, 85)
        pdf.multi_cell(170,5,"AU07 - " + str(ret[5][i][5]), 0,'L')
        
        pdf.set_xy(145, 60)
        pdf.multi_cell(170,5,"AU09 - " + str(ret[5][i][6]), 0,'L')
        pdf.set_xy(145, 65)
        pdf.multi_cell(170,5,"AU10 - " + str(ret[5][i][7]), 0,'L')
        pdf.set_xy(145, 70)
        pdf.multi_cell(170,5,"AU12 - " + str(ret[5][i][8]), 0,'L')
        pdf.set_xy(145, 75)
        pdf.multi_cell(170,5,"AU14 - " + str(ret[5][i][9]), 0,'L')
        pdf.set_xy(145, 80)
        pdf.multi_cell(170,5,"AU15 - " + str(ret[5][i][10]), 0,'L')
        pdf.set_xy(145, 85)
        pdf.multi_cell(170,5,"AU17 - " + str(ret[5][i][11]), 0,'L')
        
        pdf.set_xy(175, 60)
        pdf.multi_cell(170,5,"AU20 - " + str(ret[5][i][12]), 0,'L')
        pdf.set_xy(175, 65)
        pdf.multi_cell(170,5,"AU23 - " + str(ret[5][i][13]), 0,'L')
        pdf.set_xy(175, 70)
        pdf.multi_cell(170,5,"AU25 - " + str(ret[5][i][14]), 0,'L')
        pdf.set_xy(175, 75)
        pdf.multi_cell(170,5,"AU26 - " + str(ret[5][i][15]), 0,'L')
        pdf.set_xy(175, 80)
        pdf.multi_cell(170,5,"AU28 - " + str(ret[5][i][16]), 0,'L')
        # pdf.set_xy(180, 85)
        # pdf.multi_cell(170,5,"AU45 - " + str(ret[5][i][17]), 0,'L')
        
        ######################################### MODEL DEEP3D ##################################################
        pdf.set_font("Poppins", "", 12)        
        pdf.set_xy(20, 97)
        pdf.set_text_color(0, 113, 192)
        pdf.multi_cell(170,5,"CG Transferring Process", 0,'L')
           
        pdf.set_font("Poppins", "", 10)
        pdf.set_xy(24, 110)
        pdf.set_text_color(0, 113, 192)
        pdf.multi_cell(170,5,"Deep3D Model", 0,'L')         
        pdf.image(str(ret[2][i]), x=24, y=120, w=28) 
        
        pdf.set_text_color(0, 0, 0)        
        pdf.set_font("Poppins", "", 8)
        pdf.set_xy(60, 120)
        pdf.multi_cell(170,5,"Emotion - HAPPINESS", 0,'L')
        pdf.set_xy(60, 128)
        pdf.multi_cell(170,5,"Confident - 95%", 0,'L')
        pdf.set_xy(60, 136)
        pdf.multi_cell(170,5,"Emotion's Intensity - 76%", 0,'L')
        pdf.set_xy(60, 144)
        pdf.multi_cell(170,5,"AUs Intensity - 76%", 0,'L')
        
        pdf.set_font("Poppins", "", 8)
        pdf.set_xy(115, 120)
        pdf.multi_cell(170,5,"AU01 - " + str(ret[5][i][0]), 0,'L')
        pdf.set_xy(115, 125)
        pdf.multi_cell(170,5,"AU02 - " + str(ret[5][i][1]), 0,'L')
        pdf.set_xy(115, 130)
        pdf.multi_cell(170,5,"AU04 - " + str(ret[5][i][2]), 0,'L')
        pdf.set_xy(115, 135)
        pdf.multi_cell(170,5,"AU05 - " + str(ret[5][i][3]), 0,'L')
        pdf.set_xy(115, 140)
        pdf.multi_cell(170,5,"AU06 - " + str(ret[5][i][4]), 0,'L')
        pdf.set_xy(115, 145)
        pdf.multi_cell(170,5,"AU07 - " + str(ret[5][i][5]), 0,'L')
        
        pdf.set_xy(145, 120)
        pdf.multi_cell(170,5,"AU09 - " + str(ret[5][i][6]), 0,'L')
        pdf.set_xy(145, 125)
        pdf.multi_cell(170,5,"AU10 - " + str(ret[5][i][7]), 0,'L')
        pdf.set_xy(145, 130)
        pdf.multi_cell(170,5,"AU12 - " + str(ret[5][i][8]), 0,'L')
        pdf.set_xy(145, 135)
        pdf.multi_cell(170,5,"AU14 - " + str(ret[5][i][9]), 0,'L')
        pdf.set_xy(145, 140)
        pdf.multi_cell(170,5,"AU15 - " + str(ret[5][i][10]), 0,'L')
        pdf.set_xy(145, 145)
        pdf.multi_cell(170,5,"AU17 - " + str(ret[5][i][11]), 0,'L')
        
        pdf.set_xy(175, 120)
        pdf.multi_cell(170,5,"AU20 - " + str(ret[5][i][12]), 0,'L')
        pdf.set_xy(175, 125)
        pdf.multi_cell(170,5,"AU23 - " + str(ret[5][i][13]), 0,'L')
        pdf.set_xy(175, 130)
        pdf.multi_cell(170,5,"AU25 - " + str(ret[5][i][14]), 0,'L')
        pdf.set_xy(175, 135)
        pdf.multi_cell(170,5,"AU26 - " + str(ret[5][i][15]), 0,'L')
        pdf.set_xy(175, 140)
        pdf.multi_cell(170,5,"AU28 - " + str(ret[5][i][16]), 0,'L')
        
        pdf.set_font("Poppins", "", 10)
        pdf.set_xy(24, 160)
        pdf.set_text_color(0, 113, 192)
        pdf.multi_cell(170,5,"Deca Model", 0,'L')    
        pdf.image(str(ret[3][i]), x=26, y=170, w=23) 
        
        pdf.set_text_color(0, 0, 0)        
        pdf.set_font("Poppins", "", 8)
        pdf.set_xy(60, 170)
        pdf.multi_cell(170,5,"Emotion - HAPPINESS", 0,'L')
        pdf.set_xy(60, 178)
        pdf.multi_cell(170,5,"Confident - 95%", 0,'L')
        pdf.set_xy(60, 186)
        pdf.multi_cell(170,5,"Emotion's Intensity - 76%", 0,'L')
        pdf.set_xy(60, 194)
        pdf.multi_cell(170,5,"AUs Intensity - 76%", 0,'L')
        
        pdf.set_font("Poppins", "", 8)
        pdf.set_xy(115, 170)
        pdf.multi_cell(170,5,"AU01 - " + str(ret[5][i][0]), 0,'L')
        pdf.set_xy(115, 175)
        pdf.multi_cell(170,5,"AU02 - " + str(ret[5][i][1]), 0,'L')
        pdf.set_xy(115, 180)
        pdf.multi_cell(170,5,"AU04 - " + str(ret[5][i][2]), 0,'L')
        pdf.set_xy(115, 185)
        pdf.multi_cell(170,5,"AU05 - " + str(ret[5][i][3]), 0,'L')
        pdf.set_xy(115, 190)
        pdf.multi_cell(170,5,"AU06 - " + str(ret[5][i][4]), 0,'L')
        pdf.set_xy(115, 195)
        pdf.multi_cell(170,5,"AU07 - " + str(ret[5][i][5]), 0,'L')
        
        pdf.set_xy(145, 170)
        pdf.multi_cell(170,5,"AU09 - " + str(ret[5][i][6]), 0,'L')
        pdf.set_xy(145, 175)
        pdf.multi_cell(170,5,"AU10 - " + str(ret[5][i][7]), 0,'L')
        pdf.set_xy(145, 180)
        pdf.multi_cell(170,5,"AU12 - " + str(ret[5][i][8]), 0,'L')
        pdf.set_xy(145, 185)
        pdf.multi_cell(170,5,"AU14 - " + str(ret[5][i][9]), 0,'L')
        pdf.set_xy(145, 190)
        pdf.multi_cell(170,5,"AU15 - " + str(ret[5][i][10]), 0,'L')
        pdf.set_xy(145, 195)
        pdf.multi_cell(170,5,"AU17 - " + str(ret[5][i][11]), 0,'L')
        
        pdf.set_xy(175, 170)
        pdf.multi_cell(170,5,"AU20 - " + str(ret[5][i][12]), 0,'L')
        pdf.set_xy(175, 175)
        pdf.multi_cell(170,5,"AU23 - " + str(ret[5][i][13]), 0,'L')
        pdf.set_xy(175, 180)
        pdf.multi_cell(170,5,"AU25 - " + str(ret[5][i][14]), 0,'L')
        pdf.set_xy(175, 185)
        pdf.multi_cell(170,5,"AU26 - " + str(ret[5][i][15]), 0,'L')
        pdf.set_xy(175, 190)
        pdf.multi_cell(170,5,"AU28 - " + str(ret[5][i][16]), 0,'L')
        
        pdf.set_font("Poppins", "", 10)
        pdf.set_xy(24, 210)
        pdf.set_text_color(0, 113, 192)
        pdf.multi_cell(170,5,"Emoca Model", 0,'L')    
        pdf.image('E:/PythonProjects/tesis-view/output/deep3d/pro/happy1_mesh_deep.png', x=26, y=220, w=28) 
        
        pdf.set_text_color(0, 0, 0)        
        pdf.set_font("Poppins", "", 8)
        pdf.set_xy(60, 220)
        pdf.multi_cell(170,5,"Emotion - HAPPINESS", 0,'L')
        pdf.set_xy(60, 228)
        pdf.multi_cell(170,5,"Confident - 95%", 0,'L')
        pdf.set_xy(60, 236)
        pdf.multi_cell(170,5,"Emotion's Intensity - 76%", 0,'L')
        pdf.set_xy(60, 244)
        pdf.multi_cell(170,5,"AUs Intensity - 76%", 0,'L')
        
        pdf.set_font("Poppins", "", 8)
        pdf.set_xy(115, 220)
        pdf.multi_cell(170,5,"AU01 - " + str(ret[5][i][0]), 0,'L')
        pdf.set_xy(115, 225)
        pdf.multi_cell(170,5,"AU02 - " + str(ret[5][i][1]), 0,'L')
        pdf.set_xy(115, 230)
        pdf.multi_cell(170,5,"AU04 - " + str(ret[5][i][2]), 0,'L')
        pdf.set_xy(115, 235)
        pdf.multi_cell(170,5,"AU05 - " + str(ret[5][i][3]), 0,'L')
        pdf.set_xy(115, 240)
        pdf.multi_cell(170,5,"AU06 - " + str(ret[5][i][4]), 0,'L')
        pdf.set_xy(115, 245)
        pdf.multi_cell(170,5,"AU07 - " + str(ret[5][i][5]), 0,'L')
        
        pdf.set_xy(145, 220)
        pdf.multi_cell(170,5,"AU09 - " + str(ret[5][i][6]), 0,'L')
        pdf.set_xy(145, 225)
        pdf.multi_cell(170,5,"AU10 - " + str(ret[5][i][7]), 0,'L')
        pdf.set_xy(145, 230)
        pdf.multi_cell(170,5,"AU12 - " + str(ret[5][i][8]), 0,'L')
        pdf.set_xy(145, 235)
        pdf.multi_cell(170,5,"AU14 - " + str(ret[5][i][9]), 0,'L')
        pdf.set_xy(145, 240)
        pdf.multi_cell(170,5,"AU15 - " + str(ret[5][i][10]), 0,'L')
        pdf.set_xy(145, 245)
        pdf.multi_cell(170,5,"AU17 - " + str(ret[5][i][11]), 0,'L')
        
        pdf.set_xy(175, 220)
        pdf.multi_cell(170,5,"AU20 - " + str(ret[5][i][12]), 0,'L')
        pdf.set_xy(175, 225)
        pdf.multi_cell(170,5,"AU23 - " + str(ret[5][i][13]), 0,'L')
        pdf.set_xy(175, 230)
        pdf.multi_cell(170,5,"AU25 - " + str(ret[5][i][14]), 0,'L')
        pdf.set_xy(175, 235)
        pdf.multi_cell(170,5,"AU26 - " + str(ret[5][i][15]), 0,'L')
        pdf.set_xy(175, 240)
        pdf.multi_cell(170,5,"AU28 - " + str(ret[5][i][16]), 0,'L')
                
        ######################################### DISCOMFORT LEVEL ##################################################
        
        pdf.pagina('Confort')
        pdf.image('./resource/header-faces.png', x = 0, y = 0, w = 260, h = 26)
        pdf.set_fill_color(236, 236, 236)
        pdf.set_xy(0,0)
        pdf.set_x(20)
        pdf.cell(260, 28,'Facial Analysis', 0, 1, 'L')
        
        pdf.set_font("Poppins", "", 12)
        pdf.set_xy(20, 35)
        pdf.set_text_color(0, 113, 192)
        pdf.multi_cell(170,5,"Score Comfort Perception Human", 0,'L')
        pdf.set_font("Poppins", "", 10)
                
        pdf.set_font("Poppins", "", 10)
        pdf.set_text_color(0, 113, 192)
        pdf.set_xy(21, 36)
        pdf.multi_cell(170, 30,"DEEP3D Model", 0,'L')        
        
        pdf.image(str(ret[4][i]), x=20, y=58, w=33)
        
        pdf.image('E:/PythonProjects/tesis-app/data/output/retLime/8__exp.png', x=55, y=48, w=70)        
        
        pdf.image('E:/PythonProjects/tesis-app/data/output/retLime/8__pred.png', x=138, y=48, w=57)    
        
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Poppins", "", 10)
        pdf.set_xy(20,95)
        pdf.multi_cell(170,5,'Analysis: It was predicted by lime with 69.64% confident that the frame does NOT cause discomfort. The values of the hu1, hu6 and hu4 attributes reduce the chances of the frame having a score above 50% being considered uncomfortable. The attributes hu2 and hu0 are those that increase this probability of discomfort.', 0,'L') 
        
        pdf.set_font("Poppins", "", 10)
        pdf.set_text_color(0, 0, 0)    
        pdf.set_xy(20, 105)
        pdf.multi_cell(170, 30,"The user found the CG uncomfortable.", 0,'L')
    
        #  =============================================================================================================
            
        pdf.set_font("Poppins", "", 10)
        pdf.set_text_color(0, 113, 192)
        pdf.set_xy(21, 115)
        pdf.multi_cell(170, 30,"DECA Model", 0,'L')        
        
        pdf.image(str(ret[4][i]), x=20, y=139, w=33)
        
        pdf.image('E:/PythonProjects/tesis-app/data/output/retLime/8__exp.png', x=55, y=128, w=70)        
        
        pdf.image('E:/PythonProjects/tesis-app/data/output/retLime/8__pred.png', x=138, y=128, w=57)    
        
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Poppins", "", 10)
        pdf.set_xy(20,175)
        pdf.multi_cell(170,5,'Analysis: It was predicted by lime with 69.64% confident that the frame does NOT cause discomfort. The values of the hu1, hu6 and hu4 attributes reduce the chances of the frame having a score above 50% being considered uncomfortable. The attributes hu2 and hu0 are those that increase this probability of discomfort.', 0,'L') 
        
        pdf.set_font("Poppins", "", 10)
        pdf.set_text_color(0, 0, 0)    
        pdf.set_xy(20, 185)
        pdf.multi_cell(170, 30,"The user found the CG uncomfortable.", 0,'L')
                
        #  =============================================================================================================
        
        pdf.set_font("Poppins", "", 10)
        pdf.set_text_color(0, 113, 192)
        pdf.set_xy(21, 195)
        pdf.multi_cell(170, 30,"EMOCA Model", 0,'L')        
        
        pdf.image(str(ret[4][i]), x=20, y=215, w=33)
        
        pdf.image('E:/PythonProjects/tesis-app/data/output/retLime/8__exp.png', x=55, y=208, w=70)        
        
        pdf.image('E:/PythonProjects/tesis-app/data/output/retLime/8__pred.png', x=138, y=208, w=57)    
        
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Poppins", "", 10)
        pdf.set_xy(20,250)
        pdf.multi_cell(170,5,'Analysis: It was predicted by lime with 69.64% confident that the frame does NOT cause discomfort. The values of the hu1, hu6 and hu4 attributes reduce the chances of the frame having a score above 50% being considered uncomfortable. The attributes hu2 and hu0 are those that increase this probability of discomfort.', 0,'L') 
        
        # pdf.set_font("Poppins", "", 10)
        # pdf.set_text_color(0, 0, 0)    
        # pdf.set_xy(20, 255)
        # pdf.multi_cell(170, 30,"The user found the CG uncomfortable.", 0,'L')
        
            
    pdf.output('teste_report.pdf')
    
    return ''

def getValores():
    
    ## Session
    ## Image real
    ## Deep3D Face
    ## Deca Face
    retorno = []
    
    ## Image Real
    real = []
    session = []
    for r in os.listdir('E:/PythonProjects/tesis-view/images/'):
        session.append(r)
        for l in os.listdir('E:/PythonProjects/tesis-view/images/' + r):            
            if '.png' in l or '.jpg' in l: real.append('E:/PythonProjects/tesis-view/images/' + r + '/' + l)
    
    retorno.append(session)
    retorno.append(real)
    
    ## CG Deep3D
    cgDeep = []
    for r in os.listdir('E:/PythonProjects/tesis-view/output/deep3d/'):        
        for l in os.listdir('E:/PythonProjects/tesis-view/output/deep3d/' + r):        
            if '.png' in l or '.jpg' in l: cgDeep.append('E:/PythonProjects/tesis-view/output/deep3d/' + r + '/' + l)
            
    retorno.append(cgDeep)
    
    ## CG Deca
    cgDeca = []
    for r in os.listdir('E:/PythonProjects/tesis-view/output/deca/'):        
        for l in os.listdir('E:/PythonProjects/tesis-view/output/deca/' + r):            
            if '.jpg' not in l:                
                for s in os.listdir('E:/PythonProjects/tesis-view/output/deca/' + r + '/' + l):                    
                    if 'rendered_images-cutout' in s: cgDeca.append('E:/PythonProjects/tesis-view/output/deca/' + r + '/' + l + '/' + s)
    
    retorno.append(cgDeca)
                    
    ## CG UV's
    cgDeepUv = []
    for r in os.listdir('E:/PythonProjects/tesis-view/output/uv/deep3d/'):
        for l in os.listdir('E:/PythonProjects/tesis-view/output/uv/deep3d/' + r):
            cgDeepUv.append('E:/PythonProjects/tesis-view/output/uv/deep3d/' + r + '/' + l)
            
    retorno.append(cgDeepUv)
    
    ## OpenFace
    openFace = []
    for r in os.listdir('E:/PythonProjects/tesis-view/output/openface/real/'):
        for l in os.listdir('E:/PythonProjects/tesis-view/output/openface/real/' + r):
            for s in os.listdir('E:/PythonProjects/tesis-view/output/openface/real/' + r + '/' + l):
                if '.csv' in s:
                    arquivo = pd.read_csv('E:/PythonProjects/tesis-view/output/openface/real/' + r + '/' + l + '/' + s)                
                    valores = arquivo.iloc[:, 676:693].values
                    openFace.append(list(valores[0]))
    
    retorno.append(openFace)
    
    return retorno

if __name__=='__main__':   
        
    geraPdf()