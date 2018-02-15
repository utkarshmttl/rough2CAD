import cv2
import numpy as np


def DetectCorners(img):
    ## cvtColor = convert color
    GrayedImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    ##float32 is used for precision.
    GrayedImg = np.float32(GrayedImg)

    ## goodFeaturesToTrack(imgSource, maxNumberOfCorners, Quality, MinimumDistBetweenCorners)
    corners = cv2.goodFeaturesToTrack(GrayedImg, 200, 0.04, 50)
    corners = np.int0(corners)

    ##marking corners
    for corner in corners:
        x, y = corner.ravel()
        cv2.circle(img, (x, y), 3, 255, -1000)

    return corners, img

image = cv2.imread("../Sample/input.jpeg")

Corners, ResultImage = DetectCorners(image)
print(Corners)

cv2.imshow('ResultImage',ResultImage)
cv2.imwrite('output.jpeg',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
