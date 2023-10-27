import cv2
import mediapipe as mp # for pose estimation
import time

cap = cv2.VideoCapture(0)
# cap = cv2.VideoCapture('files/test.mp4)
ptime = 0

# pose
mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

while True:
    sucess,img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB) # to make compatible with mediapipe.
    results = pose.process(imgRGB)
    # print(results.pose_landmarks)
    # if landmarks is there, draw landmark in img.
    if results.pose_landmarks:
        # landmark points
        # mpDraw.draw_landmarks(img,results.pose_landmarks)
        # landmark points connection
        mpDraw.draw_landmarks(img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        # store landmarks and draw circle in connection
        for id,lm in enumerate(results.pose_landmarks.landmark):
            h,w,c = img.shape
            cx,cy = int(lm.x*w),int(lm.y*h)
            cv2.circle(img,(cx,cy),4,(200,10,10),cv2.FILLED)



    # frame rate
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    # display img and fps
    cv2.putText(img,'FPS : '+str(int(fps)),(20,40),cv2.FONT_HERSHEY_PLAIN,2,(255,0,0,),2)
    cv2.imshow("Output",img)

    key = cv2.waitKey(4)
    if key == ord('q'):
        break
