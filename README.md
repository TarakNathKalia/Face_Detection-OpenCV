# Face Detection using OpenCV

## 1. Project Overview
This project implements real-time face detection using OpenCV's Haar Cascade Classifier. The system captures video from a webcam, detects human faces in each frame, draws bounding boxes with labels, and records the processed video output.

## 2. Technologies Used
- Python  
- OpenCV  
- Haar Cascade Classifier  

## 3. Features
- Real-time face detection using webcam  
- Bounding boxes and labels for detected faces  
- Automatic recording of processed video (`face_detection.mp4`)  
- Clean resource handling with try-finally  

## 4. How to Run
1. Install dependencies:

```bash
pip install opencv-python
```
2. Run the script:
```bash
python face_detection.py
```
3. Use the application:  
- Press **Q** to exit the webcam window  
- The processed video will be saved as `face_detection.mp4`
## 5. Output
- Video saved: `face_detection.mp4`  
- Bounding boxes and labels appear around detected faces in real-time
