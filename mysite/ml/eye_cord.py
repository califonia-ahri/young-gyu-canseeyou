
import cv2
import numpy as np
import dlib
import pandas as pd
import os
import matplotlib.pyplot as plt

global roi
# getting where is the eye looking
cap = cv2.VideoCapture(0)
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C:\\anaconda3\\envs\\119pj\\shape_predictor_68_face_landmarks.dat") # using face dlib learing data classified by 68 dot.
eye_cascade = cv2.CascadeClassifier("C:\\119pj\\haarcascade_eye_tree_eyeglasses.xml") #use Machine learing by opencv data. if wore eye_glasses.


file = './eye_cord.csv'
if not os.path.isfile(file):
    print("no file")
    eye_cord = pd.DataFrame( [[0,480,270]],columns = ['num','x_cord' , 'y_cord'],dtype = float)

else :
    print("exist file")
    eye_cord = pd.read_csv(file,sep=",")


index,_ =eye_cord.shape

while True:
    ret, frame = cap.read()
    if ret is False:
        break
    gray_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray_roi)
    for face in faces:
        roi = frame.copy()
        landmarks = predictor(gray_roi, face)
        x1, x2, y1, y2 = face.left(),face.right(), face.top(), face.bottom()
        roi = roi[y1:y2, x1:x2] # cature face by 68dot.
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        #print(roi.size)
        #roi = roi.crop(landmarks.part(0).x,landmarks.part(24).y,landmarks.part(15).x,landmarks.part(30).y)
        roi = cv2.resize(roi,(960,540))

        eyes = eye_cascade.detectMultiScale(gray_roi)
        (ex, ey, ew, eh), _= eyes
        if ((landmarks.part(39).x- ex) >0) & (ey-eh>0) & (ex-ew>0):
            roi = frame[ey:ey+eh,ex:ex+ew].copy()
            roi = cv2.resize(roi, (960, 540))
            cv2.rectangle(frame, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)
            rows, cols, _ = roi.shape
            gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
            gray_roi = cv2.GaussianBlur(gray_roi, (7, 7), 0)

            '''src = gray_roi
            hist = cv2.calcHist([src], [0], None, [256], [0, 256])
            cv2.imshow('src', src)
            plt.plot(hist)
            plt.show()'''

            _, threshold = cv2.threshold(gray_roi, 21, 255, cv2.THRESH_BINARY_INV)
            _, contours, _ = cv2.findContours(threshold, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
            contours = sorted(contours, key=lambda x: cv2.contourArea(x), reverse=True)

            for cnt in contours:
                (x, y, w, h) = cv2.boundingRect(cnt)
                # cv2.drawContours(roi, [cnt], -1, (0,0,255),3)
                cv2.rectangle(roi, (x, y), (x + w, y + h), (255, 0, 0), 2)
                cv2.line(roi, (x + int(w / 2), 0), (x + int(w / 2), rows), (0, 255, 0), 2)
                cv2.line(roi, (0, y + int(h / 2)), (cols, y + int(h / 2)), (0, 255, 0), 2)
                print("sample = %d , %d "
                      %(
                          (landmarks.part(36).x + landmarks.part(39).x) / 2,
                          (landmarks.part(36).y + landmarks.part(39).y) / 2)
                      )
                print( "result = %d , %d\n"
                       %(x+w/2,
                         y+h/2)
                )
                print(index)
                eye_cord.loc[index] = [index,x+w/2,y+h/2]

                index+=1
                break

            cv2.imshow("Threshold", threshold)
            cv2.imshow("gray roi", gray_roi)
            cv2.imshow("roi", roi)
            cv2.imshow("Frame", frame)
        else:
            break


    key = cv2.waitKey(800)
    if key == 27:
        eye_cord.to_csv('./eye_cord.csv',index_label = ['num'],index=False)
        #########os.remove('./Image_name or path')
        break
