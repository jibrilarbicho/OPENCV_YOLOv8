import cv2
from ultralytics import YOLO
model=YOLO("yolov8n.pt")
reults=model("../images/image3.png",show=True)
cv2.waitKey(0)
cv2.destroyAllWindows()