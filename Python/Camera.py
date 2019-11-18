import cv2
import numpy as np
import math

# FPS rate needs to be faster - to be continued ;-)


class Camera:

    def __init__(self):
        self.__camera = cv2.VideoCapture(0)
        self.__camera.set(3, 320)
        self.__camera.set(4, 240)

    def getFrame(self):
        return self.__camera.read()[1]

    def getFrameHSV(self):
        # .read() gives us a tuple, where index 0 is a boolean, and index 1 is the image data.

        frame = self.__camera.read()[1]
        return cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    def medianBlur(self, frame, kernelsize):
        if kernelsize == 3:
            return self.neighbourfilter3x3(frame, 4, None)
        elif kernelsize == 5:
            return self.neighbourfilter5x5(frame, 12, None)

    def dilate(self, frame, kernelsize):
        if kernelsize == 3:
            return self.neighbourfilter3x3(frame, 8, 0)
        elif kernelsize == 5:
            return self.neighbourfilter5x5(frame, 24, 0)

    def erosion(self, frame, kernelsize):
        if kernelsize == 3:
            return self.neighbourfilter3x3(frame, 0, 255)
        elif kernelsize == 5:
            return self.neighbourfilter5x5(frame, 0, 255)

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
    def getCenterPixel(self,frame):
        width, height = frame.shape
        miny = height
        maxy = 0
        minx = width
        maxx = 0

        # -----------------------------------------------------------------------

        for y in range(height):
            for x in range(width):
                if frame[x, y] == 255:
                    if y < miny:
                        miny = y
                    elif y > maxy:
                        maxy = y
                    if x < minx:
                        minx = x
                    if x > maxx:
                        maxx = x

        avgx = int((minx + maxx) / 2)
        avgy = int((miny + maxy) / 2)
        return {avgx, avgy}
    #---------------------------------------------------------------------------

    #HSP in range function
    def Masking(self,hsvframe):
        lower_color = np.array([70, 100, 100])
        upper_color = np.array([90, 255, 255])

        mask = cv2.inRange(hsvframe, lower_color, upper_color)
        return mask