
import os
import csv
import pandas as pd

from fpdf import FPDF

def geraPdf():
    
    ret = getValores()
    for r in ret:
        print(r)
    
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
        pdf.multi_cell(170,5,"Capture 1 (Real Face)", 0,'L')
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
        pdf.set_xy(120, 38)
        pdf.multi_cell(170, 30,"Facial Action Units:", 0,'L')
        
        pdf.set_font("Poppins", "", 8)
        pdf.set_xy(120, 60)
        pdf.multi_cell(170,5,"AU01 - " + str(ret[5][i][0]), 0,'L')
        pdf.set_xy(120, 65)
        pdf.multi_cell(170,5,"AU02 - " + str(ret[5][i][1]), 0,'L')
        pdf.set_xy(120, 70)
        pdf.multi_cell(170,5,"AU04 - " + str(ret[5][i][2]), 0,'L')
        pdf.set_xy(120, 75)
        pdf.multi_cell(170,5,"AU05 - " + str(ret[5][i][3]), 0,'L')
        pdf.set_xy(120, 80)
        pdf.multi_cell(170,5,"AU06 - " + str(ret[5][i][4]), 0,'L')
        pdf.set_xy(120, 85)
        pdf.multi_cell(170,5,"AU07 - " + str(ret[5][i][5]), 0,'L')
        
        pdf.set_xy(150, 60)
        pdf.multi_cell(170,5,"AU09 - " + str(ret[5][i][6]), 0,'L')
        pdf.set_xy(150, 65)
        pdf.multi_cell(170,5,"AU10 - " + str(ret[5][i][7]), 0,'L')
        pdf.set_xy(150, 70)
        pdf.multi_cell(170,5,"AU12 - " + str(ret[5][i][8]), 0,'L')
        pdf.set_xy(150, 75)
        pdf.multi_cell(170,5,"AU14 - " + str(ret[5][i][9]), 0,'L')
        pdf.set_xy(150, 80)
        pdf.multi_cell(170,5,"AU15 - " + str(ret[5][i][10]), 0,'L')
        pdf.set_xy(150, 85)
        pdf.multi_cell(170,5,"AU17 - " + str(ret[5][i][11]), 0,'L')
        
        pdf.set_xy(180, 60)
        pdf.multi_cell(170,5,"AU20 - " + str(ret[5][i][12]), 0,'L')
        pdf.set_xy(180, 65)
        pdf.multi_cell(170,5,"AU23 - " + str(ret[5][i][13]), 0,'L')
        pdf.set_xy(180, 70)
        pdf.multi_cell(170,5,"AU25 - " + str(ret[5][i][14]), 0,'L')
        pdf.set_xy(180, 75)
        pdf.multi_cell(170,5,"AU26 - " + str(ret[5][i][15]), 0,'L')
        pdf.set_xy(180, 80)
        pdf.multi_cell(170,5,"AU28 - " + str(ret[5][i][16]), 0,'L')
        # pdf.set_xy(180, 85)
        # pdf.multi_cell(170,5,"AU45 - " + str(ret[5][i][17]), 0,'L')
        
        ######################################### MODEL DEEP3D ##################################################
        pdf.set_font("Poppins", "", 12)
        pdf.set_xy(20, 97)
        pdf.set_text_color(0, 113, 192)
        pdf.multi_cell(170,5,"Model Deep3D", 0,'L')    
        pdf.image(str(ret[2][i]), x=22, y=107, w=28) 
        
        pdf.set_xy(80, 97)
        pdf.set_text_color(0, 113, 192)
        pdf.multi_cell(170,5,"Model Deca", 0,'L')    
        pdf.image(str(ret[3][i]), x=82, y=110, w=23) 
        
        pdf.set_xy(140, 97)
        pdf.set_text_color(0, 113, 192)
        pdf.multi_cell(170,5,"Model Emoca", 0,'L')    
        pdf.image('E:/PythonProjects/tesis-view/output/deep3d/pro/happy1_mesh_deep.png', x=140, y=107, w=28) 
        
        # pdf.set_font("Poppins", "", 7)
        # pdf.set_text_color(0, 0, 0)
        # pdf.set_xy(60, 110)
        # pdf.multi_cell(170,5,"AU01 - 0.8", 0,'L')
        # pdf.set_xy(60, 115)
        # pdf.multi_cell(170,5,"AU02 - 0.9", 0,'L')
        # pdf.set_xy(60, 120)
        # pdf.multi_cell(170,5,"AU04 - 0.0", 0,'L')
        # pdf.set_xy(60, 125)
        # pdf.multi_cell(170,5,"AU05 - 0.1", 0,'L')
        # pdf.set_xy(60, 130)
        # pdf.multi_cell(170,5,"AU06 - 3.2", 0,'L')
        # pdf.image('./resource/abaixo.png', x=74, y=130.5, w=4)
        
        # pdf.set_xy(90, 110)
        # pdf.multi_cell(170,5,"AU07 - 1.2", 0,'L')    
        # pdf.set_xy(90, 115)
        # pdf.multi_cell(170,5,"AU09 - 0.5", 0,'L')
        # pdf.set_xy(90, 120)
        # pdf.multi_cell(170,5,"AU10 - 1.1", 0,'L')
        # pdf.set_xy(90, 125)
        # pdf.multi_cell(170,5,"AU12 - 2.9", 0,'L')
        # pdf.image('./resource/abaixo.png', x=104, y=125.5, w=4)
        # pdf.set_xy(90, 130)
        # pdf.multi_cell(170,5,"AU14 - 0.2", 0,'L')
        
        # pdf.set_xy(120, 110)
        # pdf.multi_cell(170,5,"AU15 - 0.0", 0,'L')
        # pdf.set_xy(120, 115)
        # pdf.multi_cell(170,5,"AU17 - 0.0", 0,'L')
        # pdf.set_xy(120, 120)
        # pdf.multi_cell(170,5,"AU20 - 0.6", 0,'L')
        # pdf.set_xy(120, 125)
        # pdf.multi_cell(170,5,"AU23 - 1.1", 0,'L')
        
        # pdf.set_xy(150, 110)
        # pdf.multi_cell(170,5,"AU25 - 1.4", 0,'L')    
        # pdf.set_xy(150, 115)
        # pdf.multi_cell(170,5,"AU26 - 1.8", 0,'L')
        # pdf.set_xy(150, 120)
        # pdf.multi_cell(170,5,"AU28 - 0.0", 0,'L')
        # pdf.set_xy(150, 125)
        # pdf.multi_cell(170,5,"AU45 - 0.0", 0,'L')
        
        ######################################### DISCOMFORT LEVEL ##################################################
        
        pdf.set_font("Poppins", "", 12)
        pdf.set_xy(20, 145)
        pdf.set_text_color(0, 113, 192)
        pdf.multi_cell(170,5,"Score Comfort Perception Human", 0,'L')
        pdf.set_font("Poppins", "", 10)
        
        pdf.set_font("Poppins", "", 10)
        pdf.set_text_color(0, 0, 0)    
        pdf.set_xy(20, 145)
        pdf.multi_cell(170, 30,"Analysis 1", 0,'L')
        
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Poppins", "", 8)
        pdf.set_xy(20,165)
        pdf.multi_cell(80,5,'As opposed to using Content here, content here, making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for lorem ipsum will uncover many web sites still in their infancy. Various versions have evolved over the years.', 0,'L')
            
        pdf.image(str(ret[4][i]), x=20, y=210, w=67)
        
        pdf.image('E:/PythonProjects/tesis-app/data/output/retLime/8__exp.png', x=100, y=160, w=72)
        
        pdf.set_font("Poppins", "", 10)
        pdf.set_text_color(0, 0, 0)    
        pdf.set_xy(110, 205)
        pdf.multi_cell(170, 30,"Analysis 2", 0,'L')
        
        pdf.set_text_color(0, 0, 0)
        pdf.set_font("Poppins", "", 8)
        pdf.set_xy(110,225)
        pdf.multi_cell(80,5,'It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it hasa more-or-less normal distribution of letters.', 0,'L')
        
        pdf.image('E:/PythonProjects/tesis-app/data/output/retLime/8__pred.png', x=115, y=260, w=57)    
        
        # pdf.set_font("Poppins", "", 12)
        # pdf.set_xy(20, 190)
        # pdf.set_text_color(0, 113, 192)
        # pdf.multi_cell(170,5,"Model DECA", 0,'L')
        # pdf.set_font("Poppins", "", 10)
        
        # pdf.image('E:/PythonProjects/tesis-view/output/deca/pro/happy1/happy1_rendered_images.jpg', x=25, y=200, w=25)
            
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