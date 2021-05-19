import cv2
from FaceDetectionModule import FaceDetector

cap = cv2.VideoCapture(0)
pTime = 0
detector = FaceDetector()
while True:
    success, img = cap.read()
    img, bboxs = detector.findFaces(img)
    # print(bboxs)

    cv2.imshow("Image", img)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break