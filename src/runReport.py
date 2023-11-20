
import os
import csv
import pandas as pd

from fpdf import FPDF

def geraPdf():
    
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
                self.image('./resource/header_capa.png')
            
        def pagina(self, label):
            self.add_page()
            self.set_font("Poppins", "", 20)
            self.set_fill_color(236, 236, 236)
            self.set_xy(20,19)
            pdf.set_text_color(0, 0, 0) 
            self.ln(4)

        def final(self):
            self.add_page()
            self.image('./fontes/barra_v.png', x = 73, y = 20, w = 3.5, h = 8)
            self.set_font("Poppins", "", 22)
            pdf.set_text_color(0, 0, 0)
            self.set_xy(75,21)
            self.cell(0, 6,'agradecemos', 0, 1, 'L')
            self.image('./fontes/logo+selo.png', x = 52.5, y =56,w=100)
            # self.image('fontes/dicas.png',15,100,w=180)
            
    # Cria pdf com dados
    pdf = PDF()
    
    pdf.add_font('Poppins','','./fontes/Poppins-Bold.ttf',uni=True)
    pdf.alias_nb_pages()
    pdf.capa()
    
    ######################################### Apresentacao ##################################################
    pdf.pagina('Olá time')
    pdf.image('./resource/header-faces.png', x = 0, y = 0, w = 260, h = 26)
    pdf.set_fill_color(236, 236, 236)
    pdf.set_xy(0,0)
    pdf.set_text_color(255, 255, 255)
    pdf.set_x(20)
    pdf.cell(260, 28,'Facial Analysis', 0, 1, 'L')

    
        
    pdf.output('teste_report.pdf')
    
    return ''

if __name__=='__main__':   
    
    geraPdf()