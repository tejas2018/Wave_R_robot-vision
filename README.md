# Wave_R_robot-vision
# 🎯 Color-Based Object Tracking and Shape Recognition using OpenCV

This project demonstrates **real-time object detection and tracking** using color filtering and shape recognition through contour detection. The script processes video frames (from a file or webcam), detects blue-colored objects, and classifies them as **circles or rectangles** based on contour approximation.

---

## 📸 Demo

> Replace these with screenshots or GIFs of your project output

| Mask (Filtered) | Detected Shapes |
|------------------|------------------|
| ![Mask](https://via.placeholder.com/150) | ![Output](https://via.placeholder.com/150) |

---

## 🧠 Features

- 🎨 HSV-based color filtering for blue objects
- 🧱 Shape recognition (rectangle/square or circle)
- 📹 Works with both webcam and video file input
- 🔄 Real-time frame processing and display
- 🖼️ Side-by-side visualization of mask and original frame

---

## 📁 Project Structure

---

## 📦 Requirements

Install the required Python libraries using pip:

```bash
pip install opencv-python opencv-contrib-python numpy matplotlib imutils
**## 🧰 Required Libraries

Make sure you have the following libraries installed for full OpenCV functionality:

| Library         | Purpose                                               |
|----------------|--------------------------------------------------------|
| `opencv-python`| Core OpenCV modules (image/video processing)           |
| `opencv-contrib-python` | Extra OpenCV modules (SIFT, SURF, etc.)     |
| `numpy`         | Efficient numerical operations on images/matrices     |
| `matplotlib` *(optional)* | Display images/plots (debugging, analysis) |
| `imutils` *(optional)* | Helper functions for image operations         |
**import cv2             # OpenCV main library
import numpy as np     # Matrix & array operations
import matplotlib.pyplot as plt  # For plotting (optional)
import imutils         # For convenience functions (optional)
## 📸 Demo

![Demo GIF](media/demo.gif)
![Detected Shapes](media/frame_example.png)

