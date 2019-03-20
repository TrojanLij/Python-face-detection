#face data manipulation
import cv2
import matplotlib.pyplot as plt
import time
import datetime

#import logging module
import logging as log
from random import *

#dir manipulation
import os
from os import walk

#import face recognition
import face_recognition

import pickle
from imutils import paths
import sys

#define function for drawing on image
def detect_faces(f_cascade, colored_img, file_name,CWDIR):
    #just making a copy of image passed, so that passed image is not changed
    img_copy = colored_img.copy()
    date_time = datetime.datetime.now()
    today_date_concat = date_time.strftime("%d") +"-"+date_time.strftime("%m")+"-"+date_time.strftime("%Y")
    logname = str(today_date_concat+".log")
    log.basicConfig(filename=logname, level=log.INFO)
    
    #convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
    font = cv2.FONT_HERSHEY_PLAIN   
    
    #let's detect multiscale (some images may be closer to camera than others) images
    faces = f_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30,30))
    #print(faces)
    #go over list of faces and draw them as rectangles on original colored img

    log.info(" "+str(file_name)+": found: "+str(len(faces))+" faces")
    log.info(" CWD: " + str(CWDIR))
    for (x, y, w, h) in faces:
        cords = str(x) +':'+ str(y)
        #cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)
        #cv2.putText(img_copy, cords, (x+3, y-5), font, 1, (200, 255, 0), 1)
        id = str(randint(1, 9999))
        cv2.imwrite("./faceData/" + str(today_date_concat) +id+ ".jpg", gray[y:y+h, x:x+w])
        location = str("[" + str(x) + " " + str(y) + " " + str(w) + " " + str(h) + "]")
        log.info("picture of: "+location+ " at: " + str(CWDIR) + "\\faceData\\" + str(today_date_concat) +id+ ".jpg")
    #log.info("face: \n[[x y w h]]\n"+str(faces)+"\n")
    log.info("\n")
    return img_copy

def pictures_in_cwd(CWD_dir):
    file_num = int(0)
    for r, d, f in os.walk(CWD_dir):
        for file in f:
            if file.endswith("jpg") or file.endswith("jpeg") or file.endswith("png"):
                file_num = file_num + 1
                #print(os.path.join(r, file))
                test1 = cv2.imread(file)
                haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
                faces_detection = detect_faces(haar_face_cascade,test1,file,CWD_dir)

                #cv2.imshow(str(file), faces_detection)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
    return file_num

def face_recon(face):
    name_of_face = ""

    #call face recognition function and insert data into DB

    return name_of_face

#get current work dir
thisdir = os.getcwd()
print(thisdir)
pictures_in_cwd(thisdir)