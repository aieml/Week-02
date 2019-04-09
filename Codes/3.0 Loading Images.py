import cv2

img=cv2.imread('Samples 1/flower.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

(height,width)=gray.shape
#print(height,width)

import random

for i in range(100):

    r=random.randint(0,height-1)
    c=random.randint(0,width-1)
    
    gray[r][c]=255

blur=cv2.blur(gray,(5,5))
ret,bw=cv2.threshold(blur,20,255,cv2.THRESH_BINARY)

cv2.imshow('IMG',img)
cv2.imshow('GRAY',gray)
cv2.imshow('BLUR',blur)
cv2.imshow('BW',bw)
