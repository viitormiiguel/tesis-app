
import os

from runTakePhoto import takePhoto
from runPreprocess import createTxtDeep
from runRender3D import render3D

def callDeep():    
    
    with open ('run.sh', 'w') as rsh:
        
        rsh.write('''\            
            #!/bin/bash
            
            source C:/Users/vitor/anaconda3/etc/profile.d/conda.sh

            conda activate deep3d

            python E:/PythonProjects/Deep3DFaceReconstruction/demo.py -i E:/PythonProjects/tesis-app/input/6585c35c1b5894e2551cd81f_0 -s E:/PythonProjects/tesis-app//output/6585c35c1b5894e2551cd81f_0

            conda deactivate
        ''')
    
    return 'OK'

def callDeca():
    
    with open ('runDeca.sh', 'w') as rsh:
        
        rsh.write('''\            
            #!/bin/bash
            
            source C:/Users/vitor/anaconda3/etc/profile.d/conda.sh

            conda activate pytorch3d

            python.exe G:/PythonProjects/DECA/demos/demo_reconstruct.py -i E:/PythonProjects/tesis-app/input/6585c35c1b5894e2551cd81f_0 -s E:/PythonProjects/tesis-app//output/6585c35c1b5894e2551cd81f_0 --useTex True --saveVis True --saveDepth True --saveObj True --saveImages True --rasterizer_type=pytorch3d

            conda deactivate
        ''')
    
    return 'OK'

if __name__ == '__main__':
    
    ## Take a picture WebCam
    # r = takePhoto()
    
    ## DECA ======================================================== ##
    callDeca()
    
    # ## DEEP 3D ====================================================== ##    
    # # PreProcess to Deep3D
    # createTxtDeep('./input/6585c35c1b5894e2551cd81f_0/')    
    # ## Run Model
    # callDeep()    
    # ## Convert to Image
    # render3D('./output/6585c35c1b5894e2551cd81f_0/')
    
   