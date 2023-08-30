
from feat.detector import Detector
from feat.data import Fex
from feat.utils.io import get_test_data_path
import matplotlib.pyplot as plt ## for visualization
import os 
import pandas as pd

detector = Detector(
    face_model="retinaface",
    landmark_model="mobilefacenet",
    au_model='xgb',
    emotion_model="resmasknet",
    facepose_model="img2pose",
)

# Helper to point to the test data folder
path = 'E:\\PythonProjects\\tesis-app\\input\\'

# Get the full path
single_face_img_path = os.path.join(path, "099_08.jpg")

single_face_prediction = detector.detect_image(single_face_img_path)

# Show results
# print(single_face_prediction.emotions)

# figs = single_face_prediction.plot_detections(poses=True, emotion_barplot=False, au_barplot=False)

figs2 = single_face_prediction.plot_detections(faces='aus-heat', muscles=True, emotion_barplot=False, au_barplot=False)

plt.show()