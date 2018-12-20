import numpy as np
import cv2 as cv
cap = cv.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()

    # Captures the video frame by frame
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', gray)
    if cv.waitKey(1) & 0xFF == ord('q'):
        # displays the resulting frame
        break

cap.release()
cap.read()
cap.isOpened()
cv.destroyAllWindows()
