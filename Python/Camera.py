import cv2


class Camera:
    __camera = cv2.VideoCapture(0)

    def getframe(self):
        frame = self.__camera.read()[1]
        return frame
