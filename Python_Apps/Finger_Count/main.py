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

board = []

# finger detector
detector = htm.HandDetector(detectionCon=0.75)

while True:
    success,img = cap.read()
    img = cv2.flip(img,1)
    # find the hand
    img = detector.findHands(img)
    # list of landark
    lmList,bbox = detector.findPosition(img,draw=True) # draw the rectangle
    # print(lmList)
    if len(lmList) !=0:
        finger = detector.fingerUp()

        # Find Distance between index and Thumb
        area = (bbox[2] - bbox[0]) * (bbox[3] - bbox[1]) // 100
        length, img, lineInfo = detector.findDistance(4, 8, img)
        cv2.putText(img,f'len : {int(length)}',(120,100),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)

        ## drawing
        if length<30:
            x1, y1, *_ = lineInfo
            board.append((x1,y1))
        
        # print(finger)
        # overlay image by slicing(image is matrix)
        # slicing 10-110 = 100 pixel and replace with image.
        img[10:110,10:110] = overlayImage[sum(finger)]
        cv2.putText(img,f'Finger: {int(sum(finger))}',(120,70),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0),2)
    
    # drawing
    for point in board:
        cv2.circle(img, point, 15, (0, 0, 0), cv2.FILLED)

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
