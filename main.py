"""
Date    :  09/11/2021
Author  :  Nipun Harsha
"""


import cv2
from cvzone.HandTrackingModule import HandDetector

cap = cv2.VideoCapture(1)
cap.set(3,1288)
#cap.set(4,720)
detector=HandDetector(detectionCon=0.8)
while True:
    Success,img=cap.read()
    img=detector.findHands(img)
    lmList,bboxInfo=detector.findPosition(img)
    cv2.rectangle(img,(100,100),(140,140),(255,210,115),cv2.FILLED)
    cv2.imshow("Image",img)
    cv2.waitKey(1)

