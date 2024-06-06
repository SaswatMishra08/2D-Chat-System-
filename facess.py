#face detection using our own self made python library
# pre requisites: termcolor, deepface, ipython, wheel, opencv, time
#sample program to check all the built in functions and features of our library which include:
#real time face detection using device camera
#real time emotion detection
#change colour of input text based on emotion captured

import facedetect
text = facedetect.textInput()
emotion = facedetect.imageCapture()
col = facedetect.colourCheck(emotion)
out= "\""+text +"\""
facedetect.display(out,col)
print("Facial Expression - "+ emotion)
