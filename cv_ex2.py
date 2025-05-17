"""
cv_ex2.py - video open

"""

import cv2
import time

# open the video 
cap = cv2.VideoCapture("robo_race.mp4")

if(cap.isOpened()):
    print("Video opened")
    # set the frame speed in cv2.waitKey
    # set the key 'q' to quit showing frames if it is pressed
    while(cv2.waitKey(30) != ord('q')):
        ret, frame = cap.read()
        # ret is True : frame got
        if ret == False:
            print("Video ends")
            break

        cv2.imshow("Video",frame)
        time.sleep(1)
        

else:
    print("Opening video failed")

cap.release()
cv2.destroyAllWindows()
