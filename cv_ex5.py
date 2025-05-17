import cv2
import numpy as np

cap = cv2.VideoCapture(0)
if cap.isOpened():
    print("webCam opened")
    while cv2.waitKey(3) != ord('q'):
        ret, frame = cap.read()
        edges = cv2.Canny(frame, 100, 200)

        lines = cv2.HoughLinesP(edges, 1, np.pi/180, 100, minLineLength=100, maxLineGap=10)
        if lines is not None:
            for x1, y1, x2, y2 in lines[:, 0, :]:
                cv2.line(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        cv2.imshow("webCam", frame)
else:
    print("Opening webCam failed")

cap.release()
cv2.destroyAllWindows()
