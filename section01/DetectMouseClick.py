import cv2
import numpy as np
image=cv2.imread("./images/cards2.jpg")
image=cv2.resize(image,(0,0),None,0.6,0.6)
count=0
circles=np.zeros((4,2),int)
def mousepoints(event,x,y,flags,param):
    global count
    if event==cv2.EVENT_LBUTTONDOWN:
        circles[count]=[x,y]
        count+=1
        print("Counter: ", count)
        print(f"Mouse Click number:{count}",circles)
        # print("Clicked at:",x,y)
while True:
    # count+=1
    # print("frame count:",count)
    if count==4:
        width,height=500,500
        pts1=np.float32([circles[0],circles[1],circles[2],circles[3]])
        pts2=np.float32([[0,0],[width,0],[0,height],[width,height]])
        matrix=cv2.getPerspectiveTransform(pts1,pts2)
        imgOutput=cv2.warpPerspective(image,matrix,(width,height))

        cv2.imshow("FinalOutput",imgOutput)
    for x in range(0,4):
        cv2.circle(image,(circles[x][0],circles[x][1]),3,(255,0,0),cv2.FILLED)
    cv2.imshow("Output",image)
    cv2.setMouseCallback("Output", mousepoints)  # Set mouse callback function to track mouse clicks
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

