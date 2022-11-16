import cv2 as cv
import numpy as np

img = cv.imread('pics/1.jpg')

cv.imshow('cat', img)

#Translation
def translate(img, x, y):
    #transMat is translation matrix
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down

translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

#Rotation
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)
    #rotation matrix
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

rotated = rotate(img, 45)
cv.imshow('Rotated', rotated)

#rotating rotated image
rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated Rotated', rotated_rotated)


#resize
#interpolation by default is INTER_AREA for shrinking image
#for enlarging INTER_LINEAR or INTER_CUBIC
#INTER_CUBIC is slower but better & HQ
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('resized', resized)


#flipping
#0 to flip vertically
#1 to flip horizontaly
flip = cv.flip(img, 0)
cv.imshow('flip', flip)


#cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)



cv.waitKey(0)




