import cv2 as cv
import numpy as np

def face_detect_demo():
    gray=cv.cvtColor(src,cv.COLOR_BGR2GRAY)
    face_detector=cv.CascadeClassifier("C:/Users/Kansx/Desktop/opencv/haarcascades/haarcascade_frontalface_alt_tree.xml")
    faces=face_detector.detectMultiScale(gray,1.10,2)
    for x,y,w,h in faces:
        cv.rectangle(src,(x,y),(x+w,y+h),(0,0,255),2)
    cv.imshow("result",src)


print("-----Hello Python-----")
src=cv.imread("C:/Users/Kansx/Desktop/opencv/img/2.jpg")
# cv.imshow("input image",src)
face_detect_demo()
cv.waitKey(0)

cv.destroyAllWindow()