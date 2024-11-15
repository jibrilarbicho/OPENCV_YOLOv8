import cv2

# Open the video capture (camera index 8)
cap = cv2.VideoCapture("../Videos/demo.mp4")
numberPlateCascade=cv2.CascadeClassifier("../haarcascades/haarcascade_russian_plate_number.xml")
count=0
# Continuously read and display the video stream
while True:
    ret, frame = cap.read()  # Read a frame from the video stream
    frame=cv2.resize(frame,(640,480))
    if ret:
        framegray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        numberplate=numberPlateCascade.detectMultiScale(framegray,1.1,4)
        for (x, y, w, h) in numberplate:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Draw a rectangle around the detected face
            cv2.putText(frame,"Number Plate",(x,y-10),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),3)
            frameOi=frame[y:y+h,x:x+w]
        cv2.imshow("Number Plate",frameOi)
        cv2.imshow("Output Stream", frame)  # Show the frame in a window
        # Wait for 1 millisecond and check if the '1' key is pressed to exit
        if cv2.waitKey(1) & 0xFF == ord('1'):
             cv2.imwrite("../Resources/NumberPlate/NoPlate_"+str(count)+".jpg", frameOi)
             cv2.rectangle(frame, (6, 288), (648, 388), (8, 255, 8), cv2.FILLED)
             cv2.putText(frame, "Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX, 2, (255, 0, 0), 2)
             cv2.imshow("Output Video", frame)
             cv2.waitKey(500)
             count += 1
        
    else:
        break

# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()