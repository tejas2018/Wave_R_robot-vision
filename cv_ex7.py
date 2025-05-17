"""
cv_ex6.py - object tracking using color filtering and shape recognition
"""

import cv2
import numpy as np

cap = cv2.VideoCapture("robo_race.mp4")

if cap.isOpened():
    print("webCam opened")
    while cv2.waitKey(3) != ord('q'):
        ret, frame = cap.read()
        if not ret:
            print("Video ended or frame not read properly.")
            break

        # Convert BGR to HSV color space
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Define lower and upper bounds for blue color
        lowBound = np.array([110, 50, 50])
        upBound = np.array([130, 255, 255])

        # Create mask for blue color
        mask = cv2.inRange(hsv, lowBound, upBound)

        # Dilation to fill gaps
        kernel = np.ones((5, 5), np.uint8)
        mask = cv2.dilate(mask, kernel, iterations=1)

        # Find contours (OpenCV 4.x)
        cnts, _ = cv2.findContours(mask.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

        # Process top 2 largest contours
        cnts = sorted(cnts, key=cv2.contourArea, reverse=True)[:2]
        for c in cnts:
            peri = cv2.arcLength(c, True)
            approx = cv2.approxPolyDP(c, 0.01 * peri, True)
            if len(approx) == 4:  # Quadrilateral
                cv2.drawContours(frame, [approx], 0, (0, 255, 0), -1)
            elif len(approx) > 10:  # Likely a circle
                cv2.drawContours(frame, [approx], 0, (0, 0, 255), -1)

        # Combine mask and original image side by side
        h1, w1 = mask.shape
        h2, w2, _ = frame.shape

        imgCom = np.zeros((max(h1, h2), w1 + w2, 3), dtype='uint8')

        # Place mask on left (convert single channel to 3-channel)
        imgCom[:h1, :w1] = cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

        # Place frame on right
        imgCom[:h2, w1:w1 + w2] = frame

        # Resize to fit original mask width
        imgCom = cv2.resize(imgCom, (w1 + w2, h1), interpolation=cv2.INTER_LINEAR)

        cv2.imshow("webCam", imgCom)
else:
    print("Opening video failed")

cap.release()
cv2.destroyAllWindows()
