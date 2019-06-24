#!/usr/bin/python
from PIL import Image
import os, sys

path = "/home/finnley/Desktop/github/New/aug_data/"
dirs = os.listdir( path )


def resize():
    for item in dirs:
        count = 1
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((800,600), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)
#            imResize.save(f +str(count)+'.jpg', 'JPEG', quality=90)
            count +=1

#cv2.imwrite("./data/phone_case"+str(count)+".jpg", image)

resize()