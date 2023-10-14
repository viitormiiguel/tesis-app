
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

import os
from pathlib import Path

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
        

if __name__ == '__main__':
    
    exportData()
