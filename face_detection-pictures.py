#face data manipulation
import cv2
import matplotlib.pyplot as plt
import time
import datetime

#import logging module
import logging as log
from random import *

#import json
import json

#dir manipulation
import os
from os import walk

#import face recognition
import face_recognition

import pickle
from imutils import paths
import sys

def get_pic():
    CWD_dir = os.getcwd()
    file_num = int(0)
    for r, d, f in os.walk(CWD_dir):
        for file in f:
            if file.endswith("jpg") or file.endswith("jpeg") or file.endswith("png"):
                file_num = file_num + 1
                #print(os.path.join(r, file))
                test1 = cv2.imread(file)
                if len(str(test1)) > 4:
                    haar_face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
                    print(str(file))
                    data_to_json_picture['picture'].append({
                        "root_path": CWD_dir,
                        "name": file,
                        "faces": detect_faces(haar_face_cascade,test1,file,CWD_dir)
                    })
    with open('data_test.json', 'w') as outfile:
        json.dump(data_to_json_picture, outfile)
    return 0

def detect_faces(f_cascade, colored_img, file_name,CWDIR):
    #just making a copy of image passed, so that passed image is not changed
    data_to_json_face = {}
    data_to_json_face['face'] = []
    img_copy = colored_img.copy()
    date_time = datetime.datetime.now()
    today_date_concat = date_time.strftime("%d") +"-"+date_time.strftime("%m")+"-"+date_time.strftime("%Y")
    logname = str(today_date_concat+".log")
    log.basicConfig(filename=logname, level=log.INFO)
    #convert the test image to gray image as opencv face detector expects gray images
    gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)
    faces = f_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=10, minSize=(10,10))
    
    log.info(" "+str(file_name)+": found: "+str(len(faces))+" faces")
    log.info(" CWD: " + str(CWDIR))
    for (x, y, w, h) in faces:
        id = str(randint(1, 9999))
        face_clip_str = str(x)+"_"+str(y)+"_"+str(w)+"_"+str(h)+"-"+str(id)+"-"+str(file_name)
        cv2.imwrite("./faceData/" + face_clip_str, gray[y:y+h, x:x+w])
        location = str("[" + str(x) + " " + str(y) + " " + str(w) + " " + str(h) + "]")
        log.info("picture of: "+location+ " at: " + str(CWDIR) + "\\faceData\\" + face_clip_str)
        data_to_json_face['face'].append({
            'face_cordinate_X': str(x),
            'face_cordinate_Y': str(y),
            'rectangle_width': str(w),
            'rectangle_height': str(h),
            'face_snippet_name': str(face_clip_str),
            'snippet_directory': str(CWDIR + "\\faceData\\")
        })
    #log.info("face: \n[[x y w h]]\n"+str(faces)+"\n")
    log.info("\n")
    return data_to_json_face

data_to_json_picture = {}
data_to_json_picture['picture'] = []
get_pic()
