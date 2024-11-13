import cv2
import numpy as np
image=cv2.imread("../images/lambo.png")
t_lower=100
t_higher=100
edge=cv2.Cany(image,t_lower,t_higher)
cv2.imshow("Gray Image",edge)
cv2.waitKey(0)