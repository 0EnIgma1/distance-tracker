import cv2
import matplotlib.pyplot as plt
import time  
import cvzone
from cvzone.FaceMeshModule import FaceMeshDetector

'''
# declaration of variables  
initialTime = 0  
initialDistance = 0  
changeInTime = 0  
changeInDistance = 0  
listDistance = []  
listSpeed = []

DECLARED_LEN = 60 # cm  
# width of the object face  
DECLARED_WID = 14.3 # cm  
# Definition of the RGB Colors format 
#Defining the fonts family, size, type  
fonts = cv2.FONT_HERSHEY_COMPLEX
'''
distance = 50
W = 6.3

def focal(w,distance,W):
    f = (w * distance) / W
    return f

f = 539
xml_data = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)
detector = FaceMeshDetector(maxFaces = 1)

def distance(f,W,w):
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
        w,_ = detector.findDistance(pointLeft,pointRight)
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
    
    cv2.putText(frame,f"distance: {distance(f,W,w)} cm",(100,50),cv2.FONT_HERSHEY_SIMPLEX,1,(255,0,0),2)
    
    cv2.imshow("fame",frame)
    
    k = cv2.waitKey(1) & 0xFF
    if k ==27:
        break
cv2.destroyAllWindows()