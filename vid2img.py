#https://medium.com/@iKhushPatel/convert-video-to-images-images-to-video-using-opencv-python-db27a128a481
#Dont forget to change the filename #19 ; I liked this one better

import numpy as np
import os
import cv2
vidcap = cv2.VideoCapture('/home/finnley/Desktop/github/New/Desitin.mp4')

try:
    if not os.path.exists('/home/finnley/Desktop/github/New/data'):
        os.makedirs('/home/finnley/Desktop/github/New/data')
except OSError:
    print ('Error: Creating directory of data')


def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:
        cv2.imwrite("/home/finnley/Desktop/github/New/data/desitin"+str(count)+".jpg", image)     # save frame as JPG file
    return hasFrames
sec = 0
frameRate = 0.5 #//it will capture image in each 0.5 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)