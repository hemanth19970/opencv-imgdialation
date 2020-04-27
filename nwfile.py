import cv2
import numpy as np


img = cv2.imread("C:\\Users\\hp\Desktop\\openn\\data\\apple.jpg")
kernel=np.ones((5,57),np.uint8)

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
blur=cv2.GaussianBlur(gray, (7,7),0)
canny=cv2.Canny(img,100,100)
imgdialation=cv2.dilate(canny,kernel,iterations=2)
cv2.imshow("pp", gray)
cv2.imshow("Fds",blur)
cv2.imshow("hdb",canny)
cv2.imshow("imgdialation",imgdialation)
cv2.waitKey(0)
