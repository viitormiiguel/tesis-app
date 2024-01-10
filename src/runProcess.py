
import os

from runTakePhoto import takePhoto
from runPreprocess import createTxtDeep
from runRender3D import render3D

from runBuildBash import callDeca
from runBuildBash import callDeep

if __name__ == '__main__':
    
    ## Take a picture WebCam
    r = takePhoto()
    
    ## DECA ======================================================== ##
    callDeca()
    
    ## DEEP 3D ====================================================== ##    
    
    # PreProcess to Deep3D
    createTxtDeep('./input/6585c35c1b5894e2551cd81f_0/')    
    
    ## Run Model
    callDeep()    
    
    ## Convert to Image
    render3D('./output/6585c35c1b5894e2551cd81f_0/')
    
    ## EMOCA
    ## callEmoca()

    ## OpenFace

    ## Modelo de emoções

    ## Scripts de Intensidades

    ## Scripts Uncanny