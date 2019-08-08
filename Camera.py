import numpy as np
import pandas as pd
import cv2

camera = cv2.VideoCapture(0)
while True:
    ret, frame = camera.read()
    cv2.imwrite("MyImg.png", frame)
    img = cv2.imread("MyImg.png")
    #cv2.imshow("Image", img)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("GrImage.png", gray)
    img2 = cv2.imread("GrImage.png")
    #cv2.imshow("Pannel", img2)
    final = np.absolute(img-img2)
    final[final >= 0]==255
    cv2.imwrite("main.png", final)
    img3 = cv2.imread("main.png")
    finalM = np.absolute(img2-img3)
    finalM[finalM >= 0]==255
    cv2.imwrite("mainImg.png", finalM)
    img4 = cv2.imread("mainImg.png")
    cv2.imshow("ImagePannel", img4)
    if cv2.waitKey(30)& 0XFF ==ord('q'):
        break
    
