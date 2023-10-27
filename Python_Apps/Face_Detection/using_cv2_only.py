import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


while True:
    success,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = faces.detectMultiScale(gray,1.3,10)

    # Draw rectange around faces
    for (x, y, w, h) in faces:
          cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    cv2.imshow('Face Detection',img)

    key = cv2.waitKey(1)
    if key == ord('q'):
        break