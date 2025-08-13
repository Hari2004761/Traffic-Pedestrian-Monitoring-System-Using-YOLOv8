# Traffic & Pedestrian Monitoring System Using YOLOv8

This project is a real-time traffic and pedestrian monitoring system that uses **YOLOv8** for object detection. It can detect vehicles, bicycles, and pedestrians in a video, display counts of each category, and highlight congestion when the number of detected objects exceeds a threshold.

## Features

- Detects multiple vehicle types: car, bus, truck, motorbike, bicycle.
- Detects pedestrians.
- Displays default YOLO bounding boxes and labels.
- Counts the number of each detected object in real-time.
- Displays a "Congestion Detected" warning when the total number of objects exceeds 10.
- Works on pre-recorded video files.

## Requirements

- Python 3.8+
- [Ultralytics YOLOv8](https://pypi.org/project/ultralytics/)
- OpenCV (`cv2`)

Install dependencies using pip:

```bash
pip install ultralytics opencv-python

Usage
Clone the repository:
git clone https://github.com/your-username/traffic-pedestrian-monitor.git
cd traffic-pedestrian-monitor
Place your video file in the project folder.

Run the script:
Video Example
The system uses YOLOv8’s default bounding boxes and labels for clear visualization of detected objects.

Notes
The congestion threshold is currently set to 10 objects. You can change it in the script:

if total_detected > 10:
    cv2.putText(annotated_frame, "Congestion Detected", (x, y),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
This project uses YOLOv8-nano (yolov8n.pt) for faster processing. You can switch to larger models for higher accuracy.
