
import os

def callDeep():    
    
    with open ('run.sh', 'w') as rsh:
        
        rsh.write('''           
            #!/bin/bash
            
            source C:/Users/vitor/anaconda3/etc/profile.d/conda.sh

            conda activate deep3d
            
            cd E:/PythonProjects/Deep3DFaceReconstruction/

            python E:/PythonProjects/Deep3DFaceReconstruction/demo.py -i E:/PythonProjects/tesis-app/input/6585c35c1b5894e2551cd81f_0 -s E:/PythonProjects/tesis-app//output/6585c35c1b5894e2551cd81f_0

            conda deactivate
        ''')
    
    return 'OK'

def callDeca():
    
    with open ('runDeca.sh', 'w') as rsh:
        
        rsh.write('''           
            #!/bin/bash
            
            source C:/Users/vitor/anaconda3/etc/profile.d/conda.sh

            conda activate pytorch3d
            
            cd G:/PythonProjects/DECA/

            python.exe G:/PythonProjects/DECA/demos/demo_reconstruct.py -i E:/PythonProjects/tesis-app/input/6585c35c1b5894e2551cd81f_0 -s E:/PythonProjects/tesis-app//output/6585c35c1b5894e2551cd81f_0 --useTex True --saveImages True --rasterizer_type=pytorch3d

            conda deactivate
        ''')
    
    return 'OK'