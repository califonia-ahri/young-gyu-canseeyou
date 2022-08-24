
'''import cv2
import numpy as np
import dlib
import pandas as pd
import os
import matplotlib.pyplot as plt
import glob
global roi
# getting where is the eye looking
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("C:\\anaconda3\\envs\\119pj\\shape_predictor_68_face_landmarks.dat") # using face dlib learing data classified by 68 dot.
eye_cascade = cv2.CascadeClassifier("C:\\119pj\\haarcascade_eye_tree_eyeglasses.xml") #use Machine learing by opencv data. if wore eye_glasses.
'''

file = '\eye_cord.csv'

def get_img(address) :
    import cv2
    import time
    print("Watch your cam, Get Img in 3 sec")
    for i in range(1,4):
        time.sleep(1)
        print(i)
    cap = cv2.VideoCapture(0)

    for i in range(0, 100):
        ret, frame = cap.read()
        i = str(i)
        path_address = address +"\\"+ i + '.PNG'
        if ret is False:
            break
        cv2.imwrite(path_address, frame)
        #print("img saved as %s" % path_address)
        time.sleep(0.1)
    print("Done\n")

def find_eye_cord(address) :
    import cv2
    import numpy as np
    import dlib
    import pandas as pd
    import os
    import matplotlib.pyplot as plt
    import glob
    global roi
    global cord_list
    print("Find eye cord")
    detector = dlib.get_frontal_face_detector()
    predictor = dlib.shape_predictor(
        "C:\\anaconda3\\envs\\119pj\\shape_predictor_68_face_landmarks.dat")  # using face dlib learing data classified by 68 dot.
    eye_cascade = cv2.CascadeClassifier(
        "C:\\119pj\\haarcascade_eye_tree_eyeglasses.xml")  # use Machine learing by opencv data. if wore eye_glasses.
    file1 = address+file
    if not os.path.isfile(address+"\*.PNG"):
        print("There is no Img file")
        print("plz put in Img in %s" % address)
        exit()
    for img in glob.glob(address+"\*.PNG"):
        if not os.path.isfile(file1):
            #print("no %s file" % file1)
            eye_cord = pd.DataFrame( [[0,480,270]],columns = ['num','x_cord' , 'y_cord'],dtype = float)

        else :
            #print("exist %s file" % file1)
            eye_cord = pd.read_csv(file1,sep=",")


        index =eye_cord.shape[0]
        frame = cv2.imread(img)

        gray_roi = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = detector(gray_roi)
        for face in faces:
            roi = frame.copy()
            roi = cv2.resize(roi, (960, 540))
            landmarks = predictor(gray_roi, face)
            x1, x2, y1, y2 = face.left(),face.right(), face.top(), face.bottom()
            roi = roi[y1:y2, x1:x2] # cature face by 68dot.
            #print(roi.size)
            #roi = roi.crop(landmarks.part(0).x,landmarks.part(24).y,landmarks.part(15).x,landmarks.part(30).y)
            roi = cv2.resize(roi,(960,540))

            eyes = eye_cascade.detectMultiScale(gray_roi)
            #print(len(eyes))
            if( (len(eyes) == 1 ) or (len(eyes) ==2) ) :
                #print(eyes[0])
                (ex, ey, ew, eh) = eyes[0]
                if ((landmarks.part(39).x- ex) >0) & (ey-eh>0) & (ex-ew>0):
                    roi = frame[ey:ey+eh,ex:ex+ew].copy()
                    roi = cv2.resize(roi, (960, 540))
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

                        #print( "result = %d , %d\n"%(x+w/2,y+h/2))
                        cord_list = ((x+w/2),(y+h/2))
                        #print(index)
                        eye_cord.loc[index] = [index, x + w / 2, y + h / 2]
                        index += 1
                        break
                else:
                    break

            else :
                continue
        #########os.remove('./Image_name or path')

        eye_cord.to_csv(file1,index_label = ['num'],index=False)
        #print("saved as %s done" % file1)
    print("Done\n")
    print(cord_list)

    return file1,cord_list

def del_img (address) :
    import os
    import glob

    print("Del Img")
    file1 = address
    for img in glob.glob(file1+"\*.PNG") :
        os.remove(img)
        #print("remove %s" % img)
    print("Done\n")
