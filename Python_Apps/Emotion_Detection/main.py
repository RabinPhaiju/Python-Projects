import cv2
import numpy as np
from tensorflow.keras.models import model_from_json

model = model_from_json(open('Python_Apps/Emotion_Detection/files/fer.json','r').read())
model.load_weights('Python_Apps/Emotion_Detection/files/fer.h5')

cap = cv2.VideoCapture(0)

labels = ('Angry','Disgust','Fear','Happy','Sad','Suprise','Neutral')

while True:
    success,full_size_image  = cap.read()
    full_size_image = cv2.flip(full_size_image,1)
    gray = cv2.cvtColor(full_size_image,cv2.COLOR_BGR2GRAY)
    faces = face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    faces = faces.detectMultiScale(gray,1.1,4)

    # Draw rectange around faces
    for (x, y, w, h) in faces:

        roi_gray = gray[y:y + h, x:x + w]
        cropped_img = np.expand_dims(np.expand_dims(cv2.resize(roi_gray, (48, 48)), -1), 0)
        cv2.normalize(cropped_img, cropped_img, alpha=0, beta=1, norm_type=cv2.NORM_L2, dtype=cv2.CV_32F)
        cv2.rectangle(full_size_image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        # Predicting the emotion
        yhat= model.predict(cropped_img)
        cv2.putText(full_size_image, labels[int(np.argmax(yhat))], (x, y-5), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow('Emotion', full_size_image)
    
    key = cv2.waitKey(4)
    if key == ord('q'):
        break