import cv2 as cv


# display video
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

while True:
    is_true, frame = capture.read()

    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destoryAllWindows()