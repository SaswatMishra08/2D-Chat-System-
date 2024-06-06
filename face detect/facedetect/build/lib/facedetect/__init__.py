
from termcolor import colored
from deepface import DeepFace
from IPython.display import clear_output
import time

import cv2

def textInput():
    string = input("Enter your text: ")
    return string

def colourCheck(txt):
    if(txt=="angry"):return 'red'
    elif(txt=="happy"):return 'green'
    elif(txt=="surprise"):return 'blue'
    elif(txt=="disgust"):return 'brown'
    elif(txt=="sad"):return 'yellow'
    elif(txt=="fear"):return 'purple'
    else: return 'black'
    
def imageCapture():
    cascPath = cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(cascPath)
    cap = cv2.VideoCapture(0)
    t_end = time.time() + 5
    while time.time() < t_end:
        ret, frame = cap.read()
        frame = cv2.flip(frame,1)
        try:
            result = DeepFace.analyze(frame, actions = ['emotion'],enforce_detection=False)
        except:
            continue
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,1.1,4)
        for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame,result['dominant_emotion'],(50,50),font,2,(0,255,0),2,cv2.LINE_4);
        cv2.imshow('Video',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cap.release()
    cv2.destroyAllWindows()
    return(result['dominant_emotion'])
def display(out,col):
    print(colored(out,col))   

# text = textInput()
# emotion = imageCapture()
# col = colourCheck(emotion)
# out= "\""+text +"\""
# print(colored(out,col))
# print("Facial Expression - "+ emotion)

