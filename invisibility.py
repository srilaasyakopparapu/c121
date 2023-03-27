import cv2
import numpy as np
fourcc=cv2.VideoWriter_fourcc(*"XVID")
output=cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))
cap=cv2.VideoCapture(0)
import time
time.sleep(2)
bg=0
for i in range(60):
    ret,bg=cap.read()
bg=np.flip(bg,axis=1)
while(cap.isOpened()):
    ret,img=cap.read()
    if not ret:
        break
    img=np.flip(img,axis=1)
    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    lowerRed=np.array([0,120,50])
    upperRed=np.array([10,255,255])
    mask1=cv2.inRange(hsv,lowerRed, upperRed)
    lowerRed=np.array([170,120,70])
    upperRed=np.array([180,255,255])
    mask2=cv2.inRange(hsv,lowerRed, upperRed)
    mask1=mask1+mask2
    cv2.imshow("mask1",mask1)
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))
    mask2 = cv2.bitwise_not(mask1)
    res1 = cv2.bitwise_and(img, img,mask=mask2)
    res2 = cv2.bitwise_and(bg, bg,mask=mask1)
    final = cv2.addWeighted(res1,1, res2,1,0)
    output.write(final)
    cv2.imshow("magic",final)
    cv2.waitKey(1)
cap.release()

cv2.destroyAllWindows()




    