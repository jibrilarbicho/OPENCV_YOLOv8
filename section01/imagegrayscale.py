import cv2
import numpy as np
image=cv2.imread("../images/lambo.png")
imageGray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image",imageGray)
cv2.waitKey(0)