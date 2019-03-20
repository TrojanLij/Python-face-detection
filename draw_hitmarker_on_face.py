import cv2
import sys
import logging as log
import datetime as dt
from time import sleep

cascPath = "haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

video_capture = cv2.VideoCapture("dictator.mp4")
anterior = 0

while True:
    if not video_capture.isOpened():
        print('Unable to load camera.')
        sleep(5)
        pass

    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    font = cv2.FONT_HERSHEY_PLAIN

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cords = str(x) +':'+ str(y)
        #cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)

        x_center = int(w/2)
        y_center = int(h/2)

        #cv2.circle(frame,(x+x_center,y+y_center), 10, (0,0,255), -1)
        cv2.line(frame, (int(x), int(y)), (x+x_center, y+y_center),(255,255,255),2)
        cv2.line(frame, (int(x+x_center), int(y+y_center)), (x, y+w),(255,255,255),2)
        cv2.line(frame, (int(x+w), int(y+h)), (x+x_center, y+y_center),(255,255,255),2)
        cv2.line(frame, (int(x+x_center), int(y+y_center)), (x+h, y),(255,255,255),2)

        #cv2.line(frame, (int(x+h), int(y+w)), (int(), int()),(255,255,255),2)

    if anterior != len(faces):
        anterior = len(faces)
        log.info("faces: "+str(len(faces))+" at "+str(dt.datetime.now()))


    # Display the resulting frame
    cv2.imshow('Video', frame)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # Display the resulting frame
    cv2.imshow('Video', frame)

# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()