import cv2 as cv
import numpy as np


img = cv.imread('pics/1.jpg')
cv.imshow('Cats', img)

blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# canny = cv.Canny(img, 125, 175)
# cv.imshow('Canny Edges', canny)

#getting contours
#cv.RETR_TREE for hierachical contours
#cv.RETR_EXTERNAL for external contours
#cv.RETR_LIST for all the contours in the image

#cv.CHAIN_APPROX is how we want to approximate the contours

ret, thresh = cv.threshold(gray, 125, 125, cv.THRESH_BINARY)
cv.imshow('Thresh',thresh)





contours, hierachies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contours found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours', blank)



cv.waitKey(0)