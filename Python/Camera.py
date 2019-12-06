import cv2
import numpy as np
import math
from win32 import win32gui

# FPS rate needs to be faster - to be continued ;-)


class Camera:

    def __init__(self):
        self.__camera = cv2.VideoCapture(0)
        self.__camera.set(3, 1280)
        self.__camera.set(4, 720)

    def getFrame(self):
        frame = self.__camera.read()[1]
        frame = cv2.resize(frame, (1280, 720))

        return cv2.flip(frame, 1)

    def getFrameLeft(self):
        frame = self.__camera.read()[1]
        frame = cv2.resize(frame, (1280, 720))
        frame = cv2.flip(frame, 1)
        # Top left
        start_row, start_col = int(0), int(0)
        # Bottom right
        end_row, end_col = int(720), int(1280 / 2)
        frame = frame[start_row:end_row, start_col:end_col]

        return frame

    def getFrameRight(self):
        frame = self.__camera.read()[1]
        frame = cv2.resize(frame, (1280, 720))
        frame = cv2.flip(frame, 1)
        # Top left
        start_row, start_col = int(0), int(1280 / 2)
        # Bottom right
        end_row, end_col = int(720), int(1280)
        frame = frame[start_row:end_row, start_col:end_col]

        return frame


    def convertToHSV(self, frame):
        return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    def medianBlur(self, frame, kernelsize):
        #  if kernelsize == 3:
        #      return self.neighbourfilter3x3(frame, 4, None)
        #  elif kernelsize == 5:
        #      return self.neighbourfilter5x5(frame, 12, None)
        return cv2.medianBlur(frame, kernelsize)

    def dilate(self, frame, kernelsize):
        #  if kernelsize == 3:
        #      return self.neighbourfilter3x3(frame, 8, 0)
        #  elif kernelsize == 5:
        #      return self.neighbourfilter5x5(frame, 24, 0)
        Kernel = np.ones((kernelsize, kernelsize), np.uint8)
        return cv2.dilate(frame, Kernel, iterations=10)

    def erosion(self, frame, kernelsize):
        #  if kernelsize == 3:
        #      return self.neighbourfilter3x3(frame, 0, 255)
        #  elif kernelsize == 5:
        #      return self.neighbourfilter5x5(frame, 0, 255)
        Kernel = np.ones((kernelsize, kernelsize), np.uint8)
        return cv2.erode(frame, Kernel, iterations=5)

    def neighbourfilter3x3(self, frame, mode, mask):
        pixelValues = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        frameOutput = np.copy(frame)
        width, height = frame.shape
        for x in range(2, (width - 1)):
            for y in range(2, (height - 1)):
                if frame[x][y] == mask or mode == 4:
                    pixelValues[0] = frame[x - 1][y - 1]
                    pixelValues[1] = frame[x][y - 1]
                    pixelValues[2] = frame[x + 1][y - 1]

                    pixelValues[3] = frame[x - 1][y]
                    pixelValues[4] = frame[x][y]
                    pixelValues[5] = frame[x + 1][y]

                    pixelValues[6] = frame[x - 1][y + 1]
                    pixelValues[7] = frame[x][y + 1]
                    pixelValues[8] = frame[x + 1][y + 1]

                    list.sort(pixelValues)
                    frameOutput[x][y] = pixelValues[mode]  # The median value.

        return frameOutput

    def neighbourfilter5x5(self, frame, mode, mask):
        pixelValues = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        frameOutput = np.copy(frame)
        width, height = frame.shape
        for x in range(3, (width - 2)):
            for y in range(3, (height - 2)):
                if frame[x][y] == mask or mode == 12:
                    pixelValues[0] = frame[x - 2][y - 2]
                    pixelValues[1] = frame[x - 1][y - 2]
                    pixelValues[2] = frame[x][y - 2]
                    pixelValues[3] = frame[x + 1][y - 2]
                    pixelValues[4] = frame[x + 2][y - 2]

                    pixelValues[5] = frame[x - 2][y - 1]
                    pixelValues[6] = frame[x - 1][y - 1]
                    pixelValues[7] = frame[x][y - 1]
                    pixelValues[8] = frame[x + 1][y - 1]
                    pixelValues[9] = frame[x + 2][y - 1]

                    pixelValues[10] = frame[x - 2][y]
                    pixelValues[11] = frame[x - 1][y]
                    pixelValues[12] = frame[x][y]
                    pixelValues[13] = frame[x + 1][y]
                    pixelValues[14] = frame[x + 2][y]

                    pixelValues[15] = frame[x - 2][y + 1]
                    pixelValues[16] = frame[x - 1][y + 1]
                    pixelValues[17] = frame[x][y + 1]
                    pixelValues[18] = frame[x + 1][y + 1]
                    pixelValues[19] = frame[x + 2][y + 1]

                    pixelValues[20] = frame[x - 2][y + 2]
                    pixelValues[21] = frame[x - 1][y + 2]
                    pixelValues[22] = frame[x][y + 2]
                    pixelValues[23] = frame[x + 1][y + 2]
                    pixelValues[24] = frame[x + 2][y + 2]

                    list.sort(pixelValues)
                    frameOutput[x][y] = pixelValues[mode]  # The median value.

        return frameOutput

    def getCenterPixel(self, frame):
        foundPixel = False
        width, height = frame.shape
        miny = height
        maxy = 0
        minx = width
        maxx = 0

        for y in range(int(height / 2)):
            for x in range(int(width / 2)):
                if frame[int(x * 2), int(y * 2)] == 255:
                    foundPixel = True
                    if y < miny:
                        miny = y
                    elif y > maxy:
                        maxy = y
                    if x < minx:
                        minx = x
                    if x > maxx:
                        maxx = x

        if foundPixel:
            avgx = int((minx + maxx) / 2)
            avgy = int((miny + maxy) / 2)
        else:
            avgx = 0
            avgy = 0

        return avgx, avgy

    def getCenterPixelCV(self, frame):
        # Might work, might not.
        M = cv2.moments(frame)
        try:
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
        except:
            cX = 0
            cY = 0

        return cX, cY

    #HSP in range function
    def Masking(self, hsvframe):
        # Frederik's webcam green values
        # lower_color = np.array([30, 50, 50])
        # upper_color = np.array([70, 255, 255])

        # Mikkel's webcam green values
        lower_color = np.array([65, 75, 75])
        upper_color = np.array([95, 255, 255])

        mask = cv2.inRange(hsvframe, lower_color, upper_color)
        return mask
