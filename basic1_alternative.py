# unlike opencv_basic1 the image is open till  either space / escape is typed

import cv2
image=cv2.imread('bw.jpg')
while True:
    cv2.imshow('alternative',image)
    k=cv2.waitKey(33)
    if k==27:
        break #27 for escape
    if k==32:
        break # 32 for space
    elif k==-1:
        continue


#ASCII CHART===>https://theasciicode.com.ar/