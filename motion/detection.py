import numpy as np
from appJar import gui
import cv2
import sys

#functions

def press(btn):
    if(btn == "Camera"):
        camera()
    else:
        print("Oops")

def open_window():
    img_path = r'G:\github\Python-face-detection\motion\trojan.png'
    img = cv2.imread(img_path, 0)
    cv2.namedWindow('camera_test1', cv2.WINDOW_NORMAL)
    cv2.imshow('camera_test1', img)
    if cv2.waitKey(0) & 0xFF == ord('q'):
            cv2.destroyAllWindows()

def camera():
    video_capture = cv2.VideoCapture(0)
    while True:
        if not video_capture.isOpened():
            print('Unable to load camera.')
            sleep(5)
            pass

        # Capture frame-by-frame
        ret, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Display the resulting frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything is done, release the capture
    video_capture.release()
    cv2.destroyAllWindows()

#open_window()

app = gui("Controls", "100x100")
app.addButton("Camera", press)
app.go()
#camera()