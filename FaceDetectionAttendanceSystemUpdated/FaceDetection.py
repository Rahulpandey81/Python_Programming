import numpy as np
import os 
import cv2
import pandas as pd
import csv
from pymysql import *
import datetime
import re
import time
Scanner = cv2.face.LBPHFaceRecognizer_create()
Scanner.read('TrainedData/trainer.yml')
xml_file = "haarcascade_frontalface_default.xml"
faceRec = cv2.CascadeClassifier(xml_file)

font = cv2.FONT_HERSHEY_SIMPLEX
id = 0
User_Names = ['None', 'Rahul', 'OneKB', 'Jay_Prakash', 'Anil']
camera = cv2.VideoCapture(0)
camera.set(3, 640)
camera.set(4, 480)
Width = 0.1*camera.get(3)
Height = 0.1*camera.get(4)
count = 0
while True:
    ret, img = camera.read()
    gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceRec.detectMultiScale(
        gray_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(Width), int(Height)),
       )

    for(x, y, w, h) in faces:

        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

        id, dt = Scanner.predict(gray_image[y:y+h, x:x+w])
        if (dt < 100):
            id = User_Names[id]
            dt = "  {0}%".format(round(100 - dt))
        else:
            id = "unknown"
            dt = "  {0}%".format(round(100 - dt))


        
        cv2.putText(img, str(id), (x+5, y-5), font, 1, (255, 255, 255), 2)
        cv2.putText(img, str(dt), (x+5, y+h-5), font, 1, (255, 255, 0), 1)

        if id in User_Names:
            f1 = open("DbFile.txt").read()
            ptrn = re.compile(id)
            mtch = ptrn.findall(f1)
            if id in mtch:
                print("Already Done Now You Can Go in the Class Room Thanks")
                break
            else:

                data = {'Date': [''], 'Name': [''], 'Attendance_Status': ['']}
                tbl = pd.DataFrame(data)
                tbl['Date'] = time.strftime("%I:%M:%S")
                tbl['Name'] = id
                tbl['Attendance_Status'] = "Present"
                f = open("DbFile.txt", 'a+')
                f.write(str(tbl))
                f.close()
                #tbl.to_csv("CSVAttendance.csv")

    #     sts = 'P'
    #     Name = 'Anurag'
    #     nm = 4
    #     nm1 = int(nm)
    #     cur.execute('insert into Sheet values(%d, "%s", "%s")' % (nm1, Name, sts))
    #     db.commit()
    #     db.close()
    # elif (id =='Abhishek Sir'):
    #     sts = 'P'
    #     Name = 'Abhishek Sir'
    #     nm = 5
    #     nm1 = int(nm)
    #     cur.execute('insert into Sheet values(%d, "%s", "%s")' % (nm1, Name, sts))
    #     db.commit()
    #     db.close()
    # elif (id == 'Ayush'):
    #     sts = 'P'
    #     Name = 'Ayush'
    #     nm = 6
    #     nm1 = int(nm)
    #     cur.execute('insert into Sheet values(%d, "%s", "%s")' % (nm1, Name, sts))
    #     db.commit()
    #     db.close()

    cv2.imshow('camera', img)
    k = cv2.waitKey(10) & 0xff
    if k == 27:
        break
print("\n Releasing the Program")
camera.release()
cv2.destroyAllWindows()

