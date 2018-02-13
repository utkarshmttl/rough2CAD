import cv2
import numpy as np

img = cv2.imread('corners.jpg')

grayed = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

grayed = np.float32(grayed)

corners = cv2.goodFeaturesToTrack(grayed,100,0.01,10)
corners = np.int0(corners)

for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,255,-1000)

cv2.imshow('corners',img)

cv2.waitKey(0)
cv2.destroyAllWindows()