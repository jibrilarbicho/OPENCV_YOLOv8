# import cv2

# # Open the video capture (camera index 8)
# cap = cv2.VideoCapture(0)
# faceCascade=cv2.CascadeClassifier("../haarcascades/haarcascade_frontalface_default.xml")

# # Continuously read and display the video stream
# while True:
#     ret, frame = cap.read()  # Read a frame from the video stream
#     if ret:
#         gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         faces=faceCascade.detectMultiScale(gray,1.1,4)
#         for (x, y, w, h) in faces:
#             cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Draw a rectangle around the detected face
#         cv2.imshow("Output Stream", frame)  # Show the frame in a window
#         # Wait for 1 millisecond and check if the '1' key is pressed to exit
#         if cv2.waitKey(1) & 0xFF == ord('1'):
#             break
#     else:
#         break

# # Release the video capture object and close all windows
# cap.release()
# cv2.destroyAllWindows()

import cv2
image=cv2.imread("../images/face.png")
# Open the video capture (camera index 8)
cap = cv2.VideoCapture(0)
faceCascade=cv2.CascadeClassifier("../haarcascades/haarcascade_frontalface_default.xml")

# Continuously read and display the video stream
gray_image= cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
faces=faceCascade.detectMultiScale(gray_image,1.1,4)
for (x, y, w, h) in faces:
  cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)  # Draw a rectangle around the detected face
cv2.imshow("Output Stream", image)  # Show the frame in a window
cv2.waitKey(0)
# Release the video capture object and close all windows
cap.release()
cv2.destroyAllWindows()
