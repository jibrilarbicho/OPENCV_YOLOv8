import cv2
import numpy as np
image1=cv2.imread("../images/cards.jpg")
image2=cv2.imread("../images/image2.jpg")
image1=cv2.resize(image1,(318,159))
print("image1 shape:",image1.shape)
print("image2 shape:",image2.shape)
imageHorizontalStck=np.hstack((image1,image2 ))
cv2.imshow("Horizontal Stack",imageHorizontalStck)
imageVerticalStck=np.vstack((image1,image2))
cv2.imshow("Vertical Stack",imageVerticalStck)
cv2.waitKey(0)
cv2.destroyAllWindows()