import numpy as np
from appJar import gui
import cv2
import sys

#functions

def nothing(x):
    pass

def camera():
    video_capture = cv2.VideoCapture(0)
    cv2.namedWindow("main_window")
    cv2.createTrackbar('R','main_window',1,255,nothing)
    cv2.createTrackbar('G','main_window',1,255,nothing)
    cv2.createTrackbar('B','main_window',1,255,nothing)
    while True:
        if not video_capture.isOpened():
            print('Unable to load camera.')
            sleep(5)
            pass

        r = cv2.getTrackbarPos('R','main_window')
        g = cv2.getTrackbarPos('G','main_window')
        b = cv2.getTrackbarPos('B','main_window')

        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_RGB2HSV)

        cv2.imshow('main_window', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

camera()