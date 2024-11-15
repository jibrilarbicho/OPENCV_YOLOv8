import cv2
import numpy as np
from pyzbar.pyzbar import decode
image=cv2.imread("./images/MultipleQR_Bar_code.PNG")
if image is None:
    print("Error: Could not open or find the image.")
    exit()

code=decode(image)
for c in code:
    print("Data:",c.data)
cv2.imshow("Output image",image)
cv2.waitKey(0)
cv2.destroyAllWindows()