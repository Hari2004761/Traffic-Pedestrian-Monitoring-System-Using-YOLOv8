import cv2
from ultralytics import YOLO


model = YOLO("yolov8n.pt")


cap = cv2.VideoCapture("video2.mp4")

tracked_classes = ["car", "bus", "truck", "motorbike", "bicycle", "person"]

while True:
    ret, frame = cap.read()
    if not ret:
        break


    results = model(frame)


    annotated_frame = results[0].plot()


    counts = {cls: 0 for cls in tracked_classes}
    for box in results[0].boxes:
        cls_id = int(box.cls[0])
        class_name = model.names[cls_id]
        if class_name in tracked_classes:
            counts[class_name] += 1


    y_pos = 30
    for obj, count in counts.items():
        cv2.putText(annotated_frame, f"{obj}: {count}", (10, y_pos),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        y_pos += 30

    # Detect congestion
    total_detected = sum(counts.values())
    frame_width = annotated_frame.shape[1]
    x = (frame_width - 200) // 2
    y = 40
    if total_detected > 10:
        cv2.putText(annotated_frame, "Congestion Detected", (x, y),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)


    cv2.imshow("Traffic & Pedestrian Detection", annotated_frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
