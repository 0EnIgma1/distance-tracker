import cv2
import matplotlib.pyplot as plt
import time  
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector
import numpy as np

#w -> the height of the detectionbox
#distance -> the initial distance through which the focal length is found
#W -> initial height of the face/object detectionbox when placed in the initial distance
 
distance = 50.0
W = 5.23
def focal(w,distance,W):
    f = (w * distance)/ W
    print(f)
    return f

f = 48 #this is found by facing face/object at 50cm distance and measuring the height of the detectionbox and passing it to the focal function

xml_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces = 1)

def distance_find(f,W,w):
    d = int((W * f) / w)
    return d

while True:
    ret , frame = cap.read()
    frame, faces = detector.findFaceMesh(frame,draw=False)
    if faces:
        face = faces[0]
        pointLeft = face[145]
        pointRight = face[374]
        #cv2.circle(frame,pointLeft,5,(0,0,255),-1)
        #cv2.circle(frame,pointRight,5,(0,0,255),-1)
        #w,_ = detector.findDistance(pointLeft,pointRight)
        #print(focal(w,distance,W))
    detecting = xml_data.detectMultiScale(frame,   
                                   minSize = (30, 30))  
    # Amount of object detected  
    amountDetecting = len(detecting)  
    # Using if condition to highlight the object detected  
    if amountDetecting != 0:  
        for (a, b, width, height) in detecting:  
            cv2.rectangle(frame, (a, b), # Highlighting detected object with rectangle  
                          (a + height, b + width),   
                          (0, 255, 0), 2)

            pixel = height
            w = pixel * 0.02645
            w = float(w)
        cv2.putText(frame,f"distance: {distance_find(f, W, w)} cm",(100,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2) #distance(f,W,w)
    
    cv2.imshow("fame",frame)
    
    k = cv2.waitKey(1) & 0xFF
    if k ==27:
        break
cv2.destroyAllWindows()