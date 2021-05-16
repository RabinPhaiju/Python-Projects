from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
from datetime import datetime

width = GetSystemMetrics(0)
height = GetSystemMetrics(1)
time_stamp = datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'Python_Apps/Screen_Recorder/{time_stamp}.mp4'

fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
capture_video = cv2.VideoWriter(file_name,fourcc,24.0,(width,height))

# Webcam
webcam = cv2.VideoCapture(0)

while True:
    # screen
    img = ImageGrab.grab(bbox=(0,0,width,height))
    img_np = np.array(img)
    img_final = cv2.cvtColor(img_np,cv2.COLOR_BGR2RGB)
    # webcam
    _,frame = webcam.read()
    fr_height,fr_width,_   = frame.shape
    # preview
    cv2.imshow('Secret Capture',img_final)
    # cv2.imshow('Webcam',frame)
    #image final
    img_final[0:fr_height,0:fr_width,:] = frame[0:fr_height,0:fr_width,:]

    capture_video.write(img_final)
    if cv2.waitKey(10) == ord('q'):
        break