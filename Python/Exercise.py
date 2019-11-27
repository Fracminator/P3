from Scene import Scene
import cv2


class Exercise(Scene):

    def __init__(self, coordinates, sceneManager, camera):
        super().__init__(sceneManager, camera)  # Call the initializing function of the superclass, aka Scene.
        self.coordinates = coordinates
        self.score = 0

    # Overrides superclass update() function
    def update(self):
        framehsv = self.camera.getFrameHSV()
        cv2.imshow("HSV", framehsv)
        mask = self.camera.Masking(framehsv)
        cv2.imshow("Mask", mask)
        median = self.camera.medianBlur(mask, 5)
        cv2.imshow("Median", median)
        erosion = self.camera.erosion(median, 5)
        cv2.imshow("Erosion", erosion)
        cv2.waitKey(1)

        # self.sceneManager.setActiveScene("Menu")  # sceneManager was inherited from the superclass.

    def validate(self, avgx, avgy, ptx, pty):
        if avgx > ptx - 25 and avgx < ptx + 25 and avgy > pty - 25 and avgy < ptx + 25:
            self.score += 1
