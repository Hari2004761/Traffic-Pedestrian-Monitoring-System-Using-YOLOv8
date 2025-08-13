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
