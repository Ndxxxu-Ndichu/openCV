import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


#resize image
img = cv.imread('pics/1.jpg')
cv.imshow('Cat', img)
resized_image = rescaleFrame(img, scale=.2)
cv.imshow('Image', resized_image)

#reading videos
capture = cv.VideoCapture('vids/1.mp4')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video Resized', frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

capture.release()
cv.destroyAllWindows()