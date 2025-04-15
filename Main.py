# Load libraries
import cv2
import face_recognition
import os
import numpy as np
from datetime import datetime
from Fonctions import findEncoding, markAttendance
def main():
    # Path of the images ' folder
    path = "ImagesBasic"
    # List of images from the folder
    images = []
    # List of images ' name
    classNames = []
    # Grab the list of images from the folder
    myList = os.listdir(path)
    # read images from the folder
    for cl in myList:
        # print(f'{path}/{cl}')
        curImg = cv2.imread(f'{path}/{cl}')
        # save image (matrix) into the array
        images.append(curImg)
        # store image's name
        classNames.append(os.path.splitext(cl)[0])
    #Encode all the images
    encodeListFinal = findEncoding(images)
    print("Images encoded successfully!")
    #print(encodeListFinal)
    #Read from camera
    cap = cv2.VideoCapture(0)
    while True:
        success, img = cap.read()
        imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25 )
        imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
        # Find face location from the webcam
        facesCurFrame = face_recognition.face_locations(imgS)
        #Encode face
        encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)
        # Find matches
        for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
            matches = face_recognition.compare_faces(encodeListFinal, encodeFace)
            faceDis = face_recognition.face_distance(encodeListFinal, encodeFace)
            # print(matches)
            # print(faceDis)
            matchIndex = np.argmin(faceDis)
            # print(matchIndex)
            if matches[matchIndex]:
                name = classNames[matchIndex].upper() # Retireve name in Uppercase
                #print(name)
                y1, x2, y2, x1 = faceLoc
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                cv2.rectangle(img, (x1,y1), (x2,y2), (0,255,0), 2)
                cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
                cv2.putText(img, name, (x1+10, y2-6 ), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255),2)
                markAttendance(name)
        cv2.imshow("Web cam", img)
        cv2.waitKey(1)


if __name__ == '__main__':
    main()
