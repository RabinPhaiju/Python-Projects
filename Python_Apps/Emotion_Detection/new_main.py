import cv2
from deepface import DeepFace
import _thread

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)
prediction =None
a = 1

def thread_prediction():
    global prediction,a
    success,img = cap.read()
    prediction = DeepFace.analyze(img,actions=['emotion'])
    a +=1
    print(a)


while True:
    success,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)


    faces = face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = faces.detectMultiScale(gray,1.1,4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
        _thread.start_new_thread(thread_prediction,())
        if isinstance(prediction,dict):
            # print(prediction['dominant_emotion'])
            cv2.putText(img,prediction['dominant_emotion'] , (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            _thread.exit()

    cv2.imshow('Emotion Detection',img)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
