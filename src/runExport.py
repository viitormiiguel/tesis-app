
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import os
from pathlib import Path
import aspose.words as aw

def exportData():    
    
    projPath = Path.cwd()
    
    path = str(projPath) + '\\model\\uv6\\lime\\'
    output = './data/output/retLime/'
        
    lista = os.listdir(path)
    
    for l in lista:
        
        print(l)
     
        n1 = l.split('_statsmodels_')
        n2 = n1[1].split('.')        
        name = n2[0]
                
        s = Service(ChromeDriverManager().install())
    
        options = Options()
        options.add_argument('headless')
        
        driver = webdriver.Chrome(service=s, options=options)
        driver.maximize_window()
        driver.get(path + l)
        
        el1 = driver.find_element(By.CLASS_NAME, 'predicted_value')
        el2 = driver.find_element(By.CLASS_NAME, 'explanation')
        
        pred    = el1.get_attribute('innerHTML')        
        exp     = el2.get_attribute('innerHTML')

        with open(output + name + "_pred.svg", "w") as svg_file:
            svg_file.write(pred)        

        with open(output + name + "_exp.svg", "w") as svg_file:
            svg_file.write(exp)
        

def runImg():
    
    output = './data/output/retLime/'
        
    lista = os.listdir(output)
    
    for l in lista:
    
        nome = l.split('.')
    
        print(nome[0])
        
        # SVG file's path
        fileName = output + l

        # create a document
        doc = aw.Document()

        # create a document builder and initialize it with document object
        builder = aw.DocumentBuilder(doc)

        # insert SVG image to document
        shape = builder.insert_image(fileName)
        
        # OPTIONAL
        # Calculate the maximum width and height and update page settings 
        # to crop the document to fit the size of the pictures.
        pageSetup = builder.page_setup
        
        if 'pred' in nome[0]:
            pageSetup.page_width = 150
        else:
            pageSetup.page_width = 180
            
        pageSetup.page_height = shape.height
        pageSetup.top_margin = 0
        pageSetup.left_margin = 0
        pageSetup.bottom_margin = 0
        pageSetup.right_margin = 0

        # save as PNG
        doc.save(output + nome[0] + ".png")
                
        # break
    

if __name__ == '__main__':
    
    exportData()
    
    runImg()
