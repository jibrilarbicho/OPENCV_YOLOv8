import cv2
import numpy as np

image=cv2.imread("./images/my4.PNG")
originlaImageCopy=image.copy()
width=700
height=700
image=cv2.resize(image,(width,height))
def prepocesing(image):
    gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    blur=cv2.GaussianBlur(gray,(5,5),0)
    canny=cv2.Canny(blur,10,70)


    return canny
def get_contours(prepocesedImage,OutputImage,minArea=100):
    contours,hierarchy=cv2.findContours(prepocesedImage.copy(),cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    rectCont=[]
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if area>minArea:
            peri=cv2.arcLength(cnt,True)
            approx=cv2.approxPolyDP(cnt,0.02*peri,True)
            if len(approx)==4:
                rectCont.append(approx)
    
    rectCont=sorted(rectCont,key=cv2.contourArea,reverse=True)
    peri1=cv2.arcLength(rectCont[0],True)
    approx1=cv2.approxPolyDP(rectCont[0],0.02*peri1,True)
    peri2=cv2.arcLength(rectCont[1],True)
    approx2=cv2.approxPolyDP(rectCont[1],0.02*peri2,True)
    approx1=reorder(approx1)
    approx2=reorder(approx2)
    print("approx1",approx1)
    print("approx2",approx2)
    cv2.drawContours(OutputImage,approx1,-1,(0,255,0),30)
    cv2.drawContours(OutputImage,approx2,-1,(0,255,0),30)

    return OutputImage,approx1,approx2
def applyThreshold(imagewrappedbuble):
    imagewarppedgrayscale=cv2.cvtColor(imagewrappedbuble ,cv2.COLOR_BGR2GRAY)
    imagewarppedThreshold=cv2.threshold(imagewarppedgrayscale,170,255,cv2.THRESH_BINARY_INV)[1]
    return imagewarppedThreshold

def splitboxes(image):
    rows=np.vsplit(image,5)
    boxes=[]
    for r in rows:
        cols=np.hsplit(r,5)
        for box in cols:
            boxes.append(box)
    return boxes
def warpperspective(Image,approx1,approx2):
    widthImg=700
    heightImg=700
    pts1=np.float32(approx1)
    pts2=np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])
    matrix=cv2.getPerspectiveTransform(pts1,pts2)
    imgwrapped=cv2.warpPerspective(Image,matrix,(widthImg,heightImg))
    ptsG=np.float32(approx2)
    ptsG2=np.float32([[0,0],[widthImg,0],[0,heightImg],[widthImg,heightImg]])

    matrix2=cv2.getPerspectiveTransform(ptsG,ptsG2)
    imgwrapped2=cv2.warpPerspective(Image,matrix2,(widthImg,heightImg))
    return imgwrapped,imgwrapped2,pts1,pts2,ptsG,ptsG2
def reorder(myPoints):
    myPoints = myPoints.reshape((4, 2))
    myPointsNew = np.zeros((4,1, 2), np.int32)

    add = myPoints.sum(1)
    print("add", add)

    myPointsNew[0] = myPoints[np.argmin(add)]
    myPointsNew[3] = myPoints[np.argmax(add)]

    diff = np.diff(myPoints, axis=1)
    myPointsNew[1] = myPoints[np.argmin(diff)]
    myPointsNew[2] = myPoints[np.argmax(diff)]

    print("New Points", myPointsNew)
    return myPointsNew


    # cv2.drawContours(OutputImage,contours,-1,(0,255,0),3)

prepocesedImage=prepocesing(image)
drwaContours,approx1,approx2=get_contours(prepocesedImage,originlaImageCopy,minArea=1000)
imgwrapped,imgwrapped2,pts1,pts2,ptsG,ptsG2=warpperspective(image,approx1,approx2)
imgwarppedThreshold=applyThreshold(imgwrapped)
boxes=splitboxes(imgwarppedThreshold)


# cv2.imshow("Warped Image",imgwrapped)
# cv2.imshow("Warped Image 2",imgwrapped2)
# cv2.imshow("Image",image)
# # # cv2.imshow("Prepocesed Image",prepocesedImage)
# cv2.imshow("Contours",drwaContours)
cv2.imshow("Threshold Image",imgwarppedThreshold)
cv2.imshow("Box",boxes[0])

cv2.waitKey(0)