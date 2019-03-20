import cv2
import sys
import logging as log
import datetime as dt
from time import sleep
import datetime
from random import *

cascPath = "./haarcascade_frontalface_alt.xml"
faceCascade = cv2.CascadeClassifier(cascPath)
log.basicConfig(filename='webcam.log',level=log.INFO)

video_capture = cv2.VideoCapture(0)
anterior = 0
date_time = datetime.datetime.now()
today_date_concat = date_time.strftime("%d") +"-"+date_time.strftime("%m")+"-"+date_time.strftime("%Y")

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

    #Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cords = str(x) +':'+ str(y)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 0), 2)
        cv2.putText(frame, cords, (x+3, y-8), font, 1, (255, 255, 0), 2)
        id = str(randint(1, 9999))
        cv2.putText(frame, "./faceData/" + str(today_date_concat) +id+ ".jpg", (5, 15), font, 1, (255, 255, 255), 2)
        #cv2.imwrite("./faceData/" + str(today_date_concat) +id+ ".jpg", gray[y:y+h, x:x+w])
    if (x, y, w, h) not in faces:
        cv2.rectangle(frame, (0, 0), (638, 478), (0, 0, 255), 5)

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