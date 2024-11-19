import cv2
import numpy as np
import pickle
width=107
height=48
with open("carparkpos","rb") as f:
        postList=pickle.load(f)
cap=cv2.VideoCapture("../Videos/video.mp4")

def checkingparkingSpace(preprocessed_frame):
    counter=0

    if len(postList)!=0:
        for pos in postList:
            x,y=pos
            croppedframe=preprocessed_frame[y:y+height,x:x+width]
            # cv2.imshow(str(x*y),croppedframe)
            count=cv2.countNonZero(croppedframe)
            if count<900:
                counter+=1
                color=(100,255,100)
            else:
                color=(100,100,255)
            cv2.rectangle(frame, (pos[0],pos[1]),(pos[0]+width,pos[1]+height),color,2)
            # cv2.putText(frame, str(count), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2, cv2.LINE_AA)
        cv2.rectangle(frame, (51, 15), (51 + width + 100, 15 + height + 16), (255, 0, 255), cv2.FILLED)
        cv2.putText(frame, f'Free: {counter}/{len(postList)}', (52, 15+height), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)



            

        
while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
     cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ret,frame=cap.read()
    if ret:
        # for pos in postList:
            # cv2.rectangle(frame, (pos[0],pos[1]),(pos[0]+width,pos[1]+height),(255,100,100),2)
        graysacle=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(graysacle,(3,3),1)
        framethreshold=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,25,16)
        medianblur=cv2.medianBlur(framethreshold,5)
        kernel=np.ones((3,3),np.uint8)
        dilate=cv2.dilate(medianblur,kernel,iterations=1)
        checkingparkingSpace(dilate)
        cv2.imshow("frame",frame)
        if cv2.waitKey(10) & 0xFF==ord('1'):
            break
    else:
        break
    
