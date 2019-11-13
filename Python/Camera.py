import cv2
import numpy as np
import math

# FPS rate needs to be faster - to be continued ;-)


class Camera:

    # The modes for neighbourfilter
    MINIMUM = 0
    MEDIAN = 4
    MAXIMUM = 8

    def __init__(self):
        self.__camera = cv2.VideoCapture(0)
        self.__camera.set(3, 320)
        self.__camera.set(4, 240)

    def getFrame(self):
        # .read() gives us a tuple, where index 0 is a boolean, and index 1 is the image data.

        frame = self.__camera.read()[1]

        width, height, channels = frame.shape

        for x in range(width):
            for y in range(height):
                blue = int(frame[x, y, 0])
                green = int(frame[x, y, 1])
                red = int(frame[x, y, 2])

                denominator = (red - green) ** 2 + (red - blue) * (green - blue)

                # Calculations for hue, saturation and intensity
                # Hue
                # to avoid divide by zero exception, an exception was made
                if denominator is not 0:
                    θ = math.acos((((red - green) + (red - blue)) / 2) / (
                        math.sqrt((red - green) ** 2 + (red - blue) * (green - blue))))

                    if green >= blue:
                        hue = θ
                    else:
                        hue = 360 - θ
                else:
                    hue = 0

                # Saturation
                # to avoid divide by zero exception, a small number is added
                saturation = (1 - (3 * (min(red, green, blue))) / (red + green + blue + 0.0000001)) * 255

                # Value
                value = max(red, green, blue)

                frame[x, y] = hue, saturation, value

        return frame

    def medianBlur(self, frame):
        return self.neighbourfilter(frame, self.MEDIAN, None)

    def dilate(self, frame):
        return self.neighbourfilter(frame, self.MAXIMUM, 0)

    def erosion(self, frame):
        return self.neighbourfilter(frame, self.MINIMUM, 255)

    def neighbourfilter(self, frame, mode, mask):
        pixelValues = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        frameOutput = np.copy(frame)
        width, height = frame.shape
        for x in range(2, (width - 1)):
            for y in range(2, (height - 1)):
                if frame[x][y] == mask or mode == self.MEDIAN:
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