import dlib
import numpy as np
import cv2
import os
import glob
import imutils
import shutil
from mtcnn import MTCNN



path = "/home/whirldata/Documents/19.10.2019/DSC_0502.JPG"
img = cv2.imread(path)
face_detector = MTCNN()
# img = adjust_gamma(img)
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
# img = adjust_gamma(img)
# img = cv2.cvtColor(img,cv2.COLOR_YCrCb2RGB)

face_info = face_detector.detect_faces(img)
for i in face_info:
    x, y, width, height = i["box"]
    cv2.rectangle(img,(x,y),(x+width,y+height),(255,0,233),3)

img = cv2.cvtColor(img,cv2.COLOR_RGB2BGR)

cv2.imwrite("face_detection.jpg",img)
print("Success")