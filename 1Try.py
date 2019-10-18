import cv2
import numpy as np
import time

cap=cv2.imread('g2.jpg')
#cap=cv2.cvtColor(cap,cv2.COLOR_RGB2HSV)
"""cap = cv2.VideoCapture(0)
width = cap.get(3)
height = cap.get(4)
fps = cap.get(5)"""
hej hej 
width,height,_=cap.shape
print(width,height)
nextID = 0
q=[]
def process (x,y,image):
    if x>0 and y>0 and x>=width and y>=height:
        return
        if y+1<height and image[y + 1, x] < 250:
            q.append((y + 1, x))
        if x+1<width and image[y, x + 1] < 250:
            q.append((y, x + 1))
        if y-1>0 and image[y - 1, x] < 250:
            q.append((y - 1, x))
        if x-1>0 and image[y, x - 1] < 250:
            q.append((x, y - 1))
while True:
   # _, frame = cap.read()
    frame=cap
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  # convert color to HSV so it actually works

    lower_color = np.array([30, 100, 100])       # lower limit of color in HSV
    upper_color = np.array([70, 255, 255])     # upper limit of color

    mask = cv2.inRange(hsv, lower_color, upper_color)       # mask that shows everything that is in our range
    result = cv2.bitwise_and(frame, frame, mask = mask)     # yeah google that

    after = cv2.medianBlur(mask, 5)
    kernel = np.ones((5, 5), np.uint8)
    morph = cv2.dilate(after, kernel, iterations=10)
    #nextID=0
    for x in range(int(width)):
        for y in range(int(height)):
            process(int(x), int(y),morph)
            while len(q) > 0:
                currentpoint = morph[x,y]
                del q[-1]
                print (currentpoint)

    print("min længde er", len(q))


    cv2.imshow('camera', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('after',after)
    cv2.imshow('result', result)
    cv2.imshow('morph', morph)

    k = cv2.waitKey(0) & 0xFF   # k waits 5ms after pressed ESC and ends the program
   # if k == 27:
    break

cv2.destroyAllWindows()  # closes windows that we created
#cap.release()            # always end capturing video