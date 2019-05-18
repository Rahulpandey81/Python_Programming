import cv2
import os

camera = cv2.VideoCapture(0)
camera.set(3, 640)
camera.set(4, 480)

trained_file = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
Face_Id = input('\n Please Enter the Numeric Value for Serial Id Number of the Face')

print("\n Please Wait While Opening Camera ...")
count = 0

while True:
    ret, img = camera.read()
    gray_Image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    Test_Faces = trained_file.detectMultiScale(gray_Image, 1.3, 5)
    for (x, y, w, h) in Test_Faces:

        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
        count += 1
        cv2.imwrite("ScannedImages/User." + str(Face_Id) + '.' + str(count) + ".jpg", gray_Image[y:y+h, x:x+w])

        cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff
    if k == 27:
        break
    elif count >= 30:
        break
print("\n Releasing Program")
camera.release()
cv2.destroyAllWindows()



