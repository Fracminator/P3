import cv2
import numpy as np


class Camera:

    def __init__(self):
        self.__camera = cv2.VideoCapture(0)
        self.__camera.set(3, 320)
        self.__camera.set(4, 240)

    def getFrame(self):
        # .read() gives us a tuple, where index 0 is a boolean, and index 1 is the image data.
        return self.__camera.read()[1]

    def medianBlur(self, frame):
        pixelValues = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        frameOutput = np.copy(frame)
        width, height = frame.shape
        for x in range(2, (width - 1)):
            for y in range(2, (height - 1)):
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
                frameOutput[x][y] = pixelValues[4]  # The median value.

        return frameOutput




