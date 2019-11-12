import cv2
import math

# FPS rate needs to be faster - to be continued ;-)

class Camera:

    def __init__(self):
        self.__camera = cv2.VideoCapture(0)
        self.__camera.set(3, 320)
        self.__camera.set(4, 240)

    def getFrame(self):
        # .read() gives us a tuple, where index 0 is a boolean, and index 1 is the image data.
        frame = self.__camera.read()[1]

        w, h, c = frame.shape

        def hsv():
            for x in range(w):
                for y in range(h):
                    blue = int(frame[x, y, 0])
                    green = int(frame[x, y, 1])
                    red = int(frame[x, y, 2])

                    denom = (red - green) ** 2 + (red - blue) * (green - blue)

                    # Calculations for hue, saturation and intensity
                    # Hue
                    # to avoid divide by zero exception, an exception was made
                    if denom is not 0:
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

            # Output img with window name as 'HSV'
            cv2.imshow('HSV', frame)

        hsv()

        if frame is not None:
            return frame
        else:
            print("ERROR: getFrame() returned empty frame.")
