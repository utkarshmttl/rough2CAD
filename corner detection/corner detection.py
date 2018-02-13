import cv2
import numpy as np
## pixel values takes bgr as params, not rgb.
img = cv2.imread('corners.jpg')
## cvtColor = convert color
grayed = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

##float32 is used for precision.
grayed = np.float32(grayed)

## goodFeaturesToTrack(imgSource, maxNumberOfCorners, Quality, MinimumDistBetweenCorners)
corners = cv2.goodFeaturesToTrack(grayed,100,0.01,10)
corners = np.int0(corners)

##marking corners
for corner in corners:
    x,y = corner.ravel()
    cv2.circle(img,(x,y),3,255,-1000)

cv2.imwrite('result.jpg',img)

cv2.imshow('corners',img)

cv2.waitKey(0)
cv2.destroyAllWindows()