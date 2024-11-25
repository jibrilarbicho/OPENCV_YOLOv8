import cv2
from ultralytics import YOLO
model=YOLO("yolov8n.pt")
classNames = model.names
cap=cv2.VideoCapture("../Videos/bikes.mp4")
import math
frame_height=int(cap.get(3))
frame_width=int(cap.get(4))
output=cv2.VideoWriter("output.avi",cv2.VideoWriter_fourcc("M","J","P","G"),10,(frame_width,frame_height))

if (cap.isOpened()==False):
    print("Error opening video file")
while (cap.isOpened()):
    ret,frame=cap.read()
    if ret:
        results=model(frame,stream=True)
        for r in results:
            boxes=r.boxes
            for box in boxes:
              x1, y1, x2, y2 = box.xyxy[0]
              print(x1, y1, x2, y2)
              x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
              cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)
              conf = math.ceil(box.conf[0] * 188) / 108
              cls = int(box.cls[0])
              class_name = classNames[cls]
              label = f'{class_name}-{conf:.2f}'
              text_size = cv2.getTextSize(label, 0, fontScale=1, thickness=2)[0]
              c2 = (x1 + text_size[0], y1 - text_size[1] - 3)
              cv2.rectangle(frame, (x1, y1), c2, [255, 0, 0], -1, cv2.LINE_AA)
              cv2.putText(frame, label, (x1, y1 - 2), 0, 1, [255, 255, 255], thickness=1, lineType=cv2.LINE_AA)

        resize_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
        output.write(resize_frame)

        cv2.imshow("frame",resize_frame)
        if cv2.waitKey(1) & 0xFF==ord('q'):
                    break
    else:
        break
cap.release()
output.release()
cv2.destroyAllWindows