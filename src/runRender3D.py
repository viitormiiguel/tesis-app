
import os

from simple_3dviz import Mesh
from simple_3dviz.window import show
from simple_3dviz.behaviours.movements import CameraTrajectory
from simple_3dviz.behaviours.trajectory import Circle
from simple_3dviz.utils import render
from simple_3dviz.behaviours.io import SaveFrames

def render3D(caminho):
    
    lista = os.listdir(caminho)
    
    for l in lista:
        
        print(l)
        
        if '.obj' in l:
            # print(caminho + l)
            m = Mesh.from_file(caminho + l, color=(0.8, 0.8, 0.8, 1.0))
            m.to_unit_cube()
            
            nome = l.split('.')            

            render(
                [m],
                n_frames=200,
                size=(256,256),
                camera_position=(0.0, 0.15, 1.5),
                up_vector=(0, 1, 0),
                behaviours=[
                    SaveFrames(caminho + nome[0] + '_deep.png')
                ]
            )

if __name__ == '__main__':
    
    path = './data/output/retDeep/'
    
    render3D(path)
    