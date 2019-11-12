import cv2


class Camera:

    def __init__(self):
        self.__camera = cv2.VideoCapture(0)

    def getFrame(self):
        # .read() gives us a tuple, where index 0 is a boolean, and index 1 is the image data.
        frame = self.__camera.read()[1]
        if frame is not None:
            return frame
        else:
            print("ERROR: getFrame() returned empty frame.")
