from ultralytics import YOLO
import cv2


model = YOLO('yolov8n.pt')


people_count = 0


LINE_X_POSITION = 320 

def process_frame(frame):
    global people_count

    frame = cv2.resize(frame, (640, 480))
    results = model(frame, verbose=False)

    for box in results[0].boxes:
        if box.cls[0] == 0 and box.conf[0] > 0.6:
            x1, y1, x2, y2 = box.xyxy[0]
            center_x, center_y = (x1 + x2) / 2, (y1 + y2) / 2


            if abs(center_x - LINE_X_POSITION) < 5:  
                people_count += 1


            cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
            cv2.putText(frame, "Person", (int(x1), int(y1) - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)


    cv2.line(frame, (LINE_X_POSITION, 0), (LINE_X_POSITION, frame.shape[0]), (255, 0, 0), 2)
    cv2.putText(frame, f"Crossings: {people_count}", (10, 30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

    return frame



cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camera")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break

    frame = process_frame(frame)
    cv2.imshow('People Counter', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
