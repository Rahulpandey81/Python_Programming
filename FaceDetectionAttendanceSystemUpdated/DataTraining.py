import cv2
import numpy as np
from PIL import Image
import os
import time
source = 'ScannedImages'
Scanner = cv2.face.LBPHFaceRecognizer_create()
detect_img = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
def StoreImages(source):
    imageSource = [os.path.join(source, f) for f in os.listdir(source)]
    faceDemos=[]
    id_Numbers = []
    for imgSrc in imageSource:
        disImage = Image.open(imgSrc).convert('L')
        npImage = np.array(disImage, 'uint8')
        id = int(os.path.split(imgSrc)[-1].split(".")[1])
        faces = detect_img.detectMultiScale(npImage)
        for (x, y, w, h) in faces:
            faceDemos.append(npImage[y:y+h, x:x+w])
            id_Numbers.append(id)
    return faceDemos, id_Numbers
start = time.time()
print("\n Data is Under Training Please Wait......")
faces, id_Numbers = StoreImages(source)
Scanner.train(faces, np.array(id_Numbers))
Scanner.write('TrainedData/trainer.yml')
print("\n {0} face trained Successfully and Detail Stored in the DataBase Thank you('.')".format(len(np.unique(id_Numbers))))
end = time.time()
print("Total Time Spend in Data Training is:-", end-start, "Seconds")
