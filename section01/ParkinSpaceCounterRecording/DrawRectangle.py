import cv2
import numpy as np
cap=cv2.VideoCapture("../Videos/video.mp4")
while True:
    ret,frame=cap.read()
    if ret:
        cv2.imshow("frame",frame)
        if cv2.waitKey(10) & 0xFF==ord('1'):
            break
    else:
        break
