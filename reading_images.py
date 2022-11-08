import cv2 as cv
#Reading Images

# img = cv.imread('pics/1.jpg')
#
# cv.imshow('Cat', img)
#
# cv.waitKey(0)

#Reading Videos

capture = cv.VideoCapture('vids/1.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()