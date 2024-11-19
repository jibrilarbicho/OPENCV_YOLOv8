import cv2
width=107
height=48
import pickle

try:
   with open("carparkpos","rb") as f:
        postList=pickle.load(f)
except:
   postList=[]
def mouseclick(events,x,y,flags,params):
    if events==cv2.EVENT_LBUTTONDOWN:
        postList.append((x,y))
    if events == cv2.EVENT_RBUTTONDOWN:
      for i, pos in enumerate(postList):
        x1, y1 = pos
        if x1 < x < x1 + width and y1 < y < y1 + height:
            postList.pop(i)
    with open("carparkpos","wb") as file:
        pickle.dump(postList,file)

while True:
   image=cv2.imread("../images/image.png")

   for pos in postList:
    cv2.rectangle(image, (pos[0],pos[1]),(pos[0]+width,pos[1]+height),(255,100,100),2)

   cv2.imshow("image",image)
   cv2.setMouseCallback("image",mouseclick)
   if cv2.waitKey(1) & 0xFF==ord('q'):
     break