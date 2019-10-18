import cv2
import numpy as np
import time
cap=cv2.imread('g2.jpg')
width,height,=cap.shape
q=[]

while True:
    frame=cap
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_color = np.array([30, 100, 100])
    upper_color = np.array([70, 255, 255])
    mask = cv2.inRange(hsv, lower_color, upper_color)
    result = cv2.bitwise_and(frame, frame, mask=mask)
