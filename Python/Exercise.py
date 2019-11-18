from Scene import Scene
import cv2


class Exercise(Scene):

    def __init__(self, coordinates, sceneManager, camera):
        super().__init__(sceneManager, camera)  # Call the initializing function of the superclass, aka Scene.
        self.coordinates = coordinates

    # Overrides superclass update() function
    def update(self):
        frame = self.camera.getFrameHSV()
        mask = self.camera.Masking(frame)
        cv2.imshow("Frame", frame)
        cv2.imshow("Mask", mask)

        # cv2.imshow("frame", frame)
        cv2.waitKey(1)
        # self.sceneManager.setActiveScene("Menu")  # sceneManager was inherited from the superclass.

    def validate(self, coordinates, step):
        place = "holder"
