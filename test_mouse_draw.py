import cv2
import numpy as np
import time

#set global var
def globvar():
    global status
    status = 0

def toggled(status_tog):
    print("toggle: "+ str(status_tog))
    if(status_tog == 1):
        status_tog = 0
        return status_tog
    elif(status_tog == 0):
        status_tog = 1
        return status_tog

def mouse_drawing(x, y):
    circles.append((x, y))
 
def mouse_click(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        #draw toggled
        toggled(status)
        print(status)
    if (int(status) == 1):
            mouse_drawing(x, y)

cap = cv2.VideoCapture(0)
 
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", mouse_click)
 
circles = []
while True:
    _, frame = cap.read()
 
    for center_position in circles:
        cv2.circle(frame, center_position, 5, (0, 0, 255), -1)
 
    cv2.imshow("Frame", frame)
 
    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("d"):
        circles = []
globvar()
cap.release()
cv2.destroyAllWindows()