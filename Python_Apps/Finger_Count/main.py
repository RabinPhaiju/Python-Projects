import cv2
import time
import os
import HandTrackingModule as htm

pTime = 0
folder_path = 'Python_Apps/Finger_Count/files'
fingerList = os.listdir(folder_path)
overlayImage = []
for imagePath in fingerList:
    image = cv2.imread(f'{folder_path}/{imagePath}')
    image = cv2.resize(image,(100,100)) #resize to 100*100
    overlayImage.append(image)

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4, 480)

# finger detector
detector = htm.HandDetector(detectionCon=0.75)

# finger landmark as picture
tipIds = [4,8,12,16,20]


while True:
    success,img = cap.read()
    # find the hand
    img = detector.findHands(img)
    # list of landark
    lmList = detector.findPosition(img,draw=False)
    # print(lmList)
    if len(lmList) !=0:
        finger = []
        # thumb
        if lmList[4][1] > lmList[4-1][1]:
                finger.append(1)
        else:
            finger.append(0)
        # other 4 finger
        for id in range(1,5):
            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                finger.append(1)
            else:
                finger.append(0)
        
        # print(finger)
        # overlay image by slicing(image is matrix)
        # slicing 10-110 = 100 pixel and replace with image.
        img[10:110,10:110] = overlayImage[sum(finger)]
        cv2.putText(img,f'Finger: {int(sum(finger))}',(120,80),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)

    # fps
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime

    # output
    cv2.putText(img,f'FPS : {int(fps)}',(120,40),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
    cv2.imshow('Output',img)

    key = cv2.waitKey(4)
    if key==ord('q'):
        break
