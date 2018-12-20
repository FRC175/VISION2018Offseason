import numpy as np
import cv2 as cv
img = cv.imread('thicc_man.jpg',0)
cv.namedWindow('thicc_man.jpg', cv.WINDOW_NORMAL)
cv.imshow('thicc_man.jpg',img)
s = cv.waitKey(0)
if s == 27:
    cv.destroyAllWindows()
elif s == ord('s'):
    cv.imwrite('thicc_boi.png',img)
    cv.destroyAllWindows()
