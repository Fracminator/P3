import cv2


class Camera:
    __camera = cv2.VideoCapture(0)

    def getFrame(self):
        # .read() gives us a tuple, where index 0 is a boolean, and index 1 is the image data.
        cameraData = self.__camera.read()
        readCorrectly = cameraData[0]
        image = cameraData[1]

        # The boolean is true if the image was read properly, so we check for that, and then return the image data.
        if readCorrectly:
            return image
        else:
            print("ERROR: getFrame() failed. Image not read correctly")
