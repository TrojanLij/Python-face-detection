import numpy as np
from appJar import gui
import cv2
import sys
import datetime
from random import *

#functions

def nothing(x):
    pass

def camera():
    cascPath = "../haarcascade_frontalface_alt.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    video_capture = cv2.VideoCapture(0)
    cv2.namedWindow("main_window")
    cv2.createTrackbar('R','main_window',0,255,nothing)
    cv2.createTrackbar('G','main_window',0,255,nothing)
    cv2.createTrackbar('B','main_window',0,255,nothing)
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
        font = cv2.FONT_HERSHEY_PLAIN

        faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.2,
            minNeighbors=5,
            minSize=(30, 30)
        )

        for (x, y, w, h) in faces:
            color = [b,g,r]
            cords = str(x) +':'+ str(y)
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, cords, (x+3, y-8), font, 1, color, 2)
            if (x, y, w, h) not in faces:
                cv2.rectangle(frame, (0, 0), (638, 478), (0, 0, 255), 5)

        cv2.imshow('main_window', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

camera()